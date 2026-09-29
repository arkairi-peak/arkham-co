/* Molten gold: a WebGL shader of slow liquid metal that the pointer can stir.
   One instance fills the hero arch (and pours in during loading); another lives inside the letters of the
   closing headline, using a text mask. No libraries.

   Stirring is a small fluid-like "wake" simulation on a low-resolution texture: the pointer pushes velocity into
   it, the velocity drifts along itself, spreads and fades. The gold is then displaced by that field, so moving the
   pointer drags the liquid and leaves a trail that settles, instead of twisting it rigidly. */
(function () {
  "use strict";

  var VERT = "attribute vec2 p;void main(){gl_Position=vec4(p,0.0,1.0);}";

  var PRECISION = ["#ifdef GL_FRAGMENT_PRECISION_HIGH", "precision highp float;", "#else", "precision mediump float;", "#endif"].join("\n");

  // Wake simulation: velocity in R/G (0.5 = still), advected by itself, diffused, decayed, plus the pointer's push.
  var SIM_FRAG = [
    PRECISION,
    "uniform sampler2D uPrev;",
    "uniform vec2 uSimRes;",
    "uniform vec2 uSize;",
    "uniform vec2 uMouse;",
    "uniform vec2 uVel;",
    "uniform float uRadius;",
    "uniform float uDecay;",
    "vec2 dec(vec4 c){return c.xy*2.0-1.0;}",
    "void main(){",
    "  vec2 uv=gl_FragCoord.xy/uSimRes;",
    "  vec2 t=1.0/uSimRes;",
    "  vec2 v0=dec(texture2D(uPrev,uv));",
    "  vec2 back=uv-v0*t*2.5;",
    "  vec2 c=dec(texture2D(uPrev,back));",
    "  vec2 n=dec(texture2D(uPrev,back+vec2(t.x,0.0)))+dec(texture2D(uPrev,back-vec2(t.x,0.0)))",
    "        +dec(texture2D(uPrev,back+vec2(0.0,t.y)))+dec(texture2D(uPrev,back-vec2(0.0,t.y)));",
    "  vec2 v=mix(c,n*0.25,0.5)*uDecay;",
    "  vec2 d=(uv-uMouse)*uSize;",
    "  v+=uVel*exp(-dot(d,d)/(uRadius*uRadius));",
    // Nudge tiny values to zero so 8-bit storage never leaves a frozen ripple behind.
    "  v=sign(v)*max(abs(v)-0.006,0.0);",
    "  v=clamp(v,-1.0,1.0);",
    "  gl_FragColor=vec4(v*0.5+0.5,0.0,1.0);",
    "}",
  ].join("\n");

  var FRAG = [
    PRECISION,
    "uniform vec2 uRes;",
    "uniform float uTime;",
    "uniform float uCool;",
    "uniform float uZoom;",
    "uniform float uFill;",
    "uniform float uBright;",
    "uniform float uScale;",
    "uniform vec4 uArch;",
    "uniform vec2 uLight;",
    "uniform sampler2D uWake;",
    "uniform float uWakeAmp;",
    "uniform sampler2D uMask;",
    "uniform float uUseMask;",

    // 2D simplex noise (Ashima Arts / Stefan Gustavson, MIT)
    "vec3 permute(vec3 x){return mod(((x*34.0)+1.0)*x,289.0);}",
    "float snoise(vec2 v){",
    "  const vec4 C=vec4(0.211324865405187,0.366025403784439,-0.577350269189626,0.024390243902439);",
    "  vec2 i=floor(v+dot(v,C.yy));vec2 x0=v-i+dot(i,C.xx);",
    "  vec2 i1=(x0.x>x0.y)?vec2(1.0,0.0):vec2(0.0,1.0);",
    "  vec4 x12=x0.xyxy+C.xxzz;x12.xy-=i1;i=mod(i,289.0);",
    "  vec3 p=permute(permute(i.y+vec3(0.0,i1.y,1.0))+i.x+vec3(0.0,i1.x,1.0));",
    "  vec3 m=max(0.5-vec3(dot(x0,x0),dot(x12.xy,x12.xy),dot(x12.zw,x12.zw)),0.0);",
    "  m=m*m;m=m*m;",
    "  vec3 x=2.0*fract(p*C.www)-1.0;vec3 h=abs(x)-0.5;vec3 ox=floor(x+0.5);vec3 a0=x-ox;",
    "  m*=1.79284291400159-0.85373472095314*(a0*a0+h*h);",
    "  vec3 g;g.x=a0.x*x0.x+h.x*x0.y;g.yz=a0.yz*x12.xz+h.yz*x12.yw;",
    "  return 130.0*dot(m,g);",
    "}",
    "float fbm(vec2 p){",
    "  float f=0.0;float a=0.5;",
    "  for(int i=0;i<4;i++){f+=a*snoise(p);p=mat2(0.8,0.6,-0.6,0.8)*p*2.01;a*=0.42;}",
    "  return f;",
    "}",
    "float fbm3(vec2 p){",
    "  float f=0.0;float a=0.5;",
    "  for(int i=0;i<3;i++){f+=a*snoise(p);p=mat2(0.8,0.6,-0.6,0.8)*p*2.03;a*=0.5;}",
    "  return f;",
    "}",

    "void main(){",
    "  vec2 frag=gl_FragCoord.xy;",
    "  vec2 uv=frag/uRes;",
    "  vec2 p=(frag-0.5*uRes)/uRes.y*uZoom;",
    // The wake drags the liquid along with the pointer, with a slight curl.
    "  vec2 wk=texture2D(uWake,uv).xy*2.0-1.0;",
    "  float stir=length(wk);",
    "  p-=(wk+vec2(-wk.y,wk.x)*0.35)*uWakeAmp;",
    "  float t=uTime*0.045;",
    "  vec2 q=vec2(fbm3(p+vec2(0.0,t)),fbm3(p+vec2(5.2,1.3)-t*0.8));",
    "  vec2 r=vec2(fbm3(p+1.5*q+vec2(1.7,9.2)+t*0.9),fbm3(p+1.5*q+vec2(8.3,2.8)-t*0.7));",
    "  vec2 w=p+1.35*r;",
    "  float h=fbm(w);",
    "  float e=0.03;",
    "  float hx=fbm(w+vec2(e,0.0));",
    "  float hy=fbm(w+vec2(0.0,e));",
    "  vec3 n=normalize(vec3((h-hx)/e*0.17,(h-hy)/e*0.17,1.0));",
    "  vec3 L=normalize(vec3(uLight,0.85));",
    "  vec3 H=normalize(L+vec3(0.0,0.0,1.0));",
    "  float diff=clamp(dot(n,L),0.0,1.0);",
    "  float nh=clamp(dot(n,H),0.0,1.0);",
    "  float spec=pow(nh,48.0);",
    "  float sheen=pow(nh,7.0);",
    "  float m=clamp(0.52+0.55*h+0.22*length(q)+uBright,0.0,1.0);",
    "  vec3 deep=vec3(0.075,0.05,0.022);",
    "  vec3 bronze=vec3(0.40,0.27,0.11);",
    "  vec3 gold=vec3(0.80,0.62,0.33);",
    "  vec3 pale=vec3(1.0,0.90,0.66);",
    "  vec3 col=mix(deep,bronze,smoothstep(0.08,0.42,m));",
    "  col=mix(col,gold,smoothstep(0.34,0.78,m));",
    "  col*=0.42+0.82*diff;",
    // Stirred metal catches a little more light.
    "  col+=pale*spec*(1.15+stir*0.9)+gold*sheen*0.32;",
    "  col+=vec3(0.95,0.78,0.48)*pow(1.0-n.z,2.0)*0.55;",
    // Cooling: the gold turns to dark bronze with only its highlights left.
    "  vec3 cold=deep*0.42+vec3(0.62,0.48,0.26)*spec*0.45+vec3(0.20,0.15,0.08)*sheen*0.10;",
    "  col=mix(col,cold,uCool);",
    "  col*=0.84+0.16*smoothstep(0.95,0.2,length(uv-0.5));",
    "  float alpha=1.0;",
    // Pouring: a wavy surface rises from the bottom of the arch.
    "  if(uFill<1.05){",
    "    float k=1.0-clamp(uFill,0.0,1.0);",
    "    float s=uArch.y+uArch.w*uFill*1.08+(sin(frag.x*0.016/uScale+uTime*2.2)*7.0+sin(frag.x*0.043/uScale-uTime*3.3)*3.5)*uScale*k;",
    "    alpha=smoothstep(s+1.5*uScale,s-1.5*uScale,frag.y);",
    "    col+=pale*smoothstep(9.0*uScale,0.0,abs(frag.y-s))*0.8*k;",
    "  }",
    "  if(uUseMask>0.5){alpha*=texture2D(uMask,uv).a;}",
    "  gl_FragColor=vec4(col*alpha,alpha);",
    "}",
  ].join("\n");

  function compile(gl, type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      var log = gl.getShaderInfoLog(s);
      gl.deleteShader(s);
      throw new Error("Gold shader: " + log);
    }
    return s;
  }

  function program(gl, frag, names) {
    var prog = gl.createProgram();
    gl.attachShader(prog, compile(gl, gl.VERTEX_SHADER, VERT));
    gl.attachShader(prog, compile(gl, gl.FRAGMENT_SHADER, frag));
    gl.bindAttribLocation(prog, 0, "p");
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error("Gold shader link: " + gl.getProgramInfoLog(prog));
    var loc = {};
    for (var i = 0; i < names.length; i++) loc[names[i]] = gl.getUniformLocation(prog, names[i]);
    return { prog: prog, loc: loc };
  }

  function texture(gl, w, h, data) {
    var tex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, data || null);
    return tex;
  }

  function GoldLiquid(canvas, options) {
    var o = options || {};
    this.canvas = canvas;
    this.quality = o.quality || 0.6;
    this.minQuality = o.minQuality || 0.3;
    this.maxDpr = o.maxDpr || 1.5;
    this.useMask = Boolean(o.mask);
    this.static = Boolean(o.static);
    this.wakeRadius = o.wakeRadius || 70; // px
    this.wakeAmp = o.wakeAmp || 0.24;

    var gl = canvas.getContext("webgl", { alpha: true, premultipliedAlpha: true, antialias: false, depth: false, stencil: false, powerPreference: "high-performance" });
    if (!gl) throw new Error("WebGL unavailable");
    this.gl = gl;

    this.main = program(gl, FRAG, ["uRes", "uTime", "uCool", "uZoom", "uFill", "uBright", "uScale", "uArch", "uLight", "uWake", "uWakeAmp", "uMask", "uUseMask"]);
    this.sim = program(gl, SIM_FRAG, ["uPrev", "uSimRes", "uSize", "uMouse", "uVel", "uRadius", "uDecay"]);

    var buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0);
    gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

    // Values the page animates.
    this.cool = 0;
    this.zoom = o.zoom || 1.5;
    this.fill = o.fill == null ? 2 : o.fill;
    this.bright = o.bright || 0;
    this.arch = { left: 0, top: 0, width: 0, height: 0 }; // CSS px, relative to the canvas
    this.light = [-0.4, 0.6];
    this.lightTarget = [-0.4, 0.6];

    // Pointer: the raw position and a smoothed one that the wake follows, so jittery input still draws a clean path.
    this.ptr = null;
    this.sm = null;
    this.prevSm = null;
    this.vel = [0, 0];

    this.wake = { w: 0, h: 0, tex: [], fb: [], i: 0 };
    this.visible = true;
    this.running = false;
    this.t0 = performance.now();
    this.frames = [];

    this.maskTex = texture(gl, 1, 1, new Uint8Array([0, 0, 0, 0]));

    var self = this;
    this.loop = function () {
      if (!self.running) return;
      self.render();
      self.raf = requestAnimationFrame(self.loop);
    };

    this.resize();
    if ("ResizeObserver" in window) new ResizeObserver(function () { self.resize(); }).observe(canvas);
    else window.addEventListener("resize", function () { self.resize(); });

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        self.visible = entries[0].isIntersecting;
        self.update();
      }).observe(canvas);
    }
    document.addEventListener("visibilitychange", function () { self.update(); });
    canvas.addEventListener("webglcontextlost", function (e) {
      e.preventDefault();
      self.lost = true;
      self.update();
      if (self.onLost) self.onLost();
    });
  }

  GoldLiquid.prototype.resize = function () {
    var gl = this.gl;
    var r = this.canvas.getBoundingClientRect();
    this.cssW = Math.max(1, r.width);
    this.cssH = Math.max(1, r.height);
    this.scale = Math.min(window.devicePixelRatio || 1, this.maxDpr) * this.quality;
    var w = Math.max(1, Math.round(this.cssW * this.scale));
    var h = Math.max(1, Math.round(this.cssH * this.scale));
    if (this.canvas.width !== w || this.canvas.height !== h) {
      this.canvas.width = w;
      this.canvas.height = h;
    }

    // The wake runs at about one texel per 6 CSS pixels; it is smooth, so that is plenty.
    var sw = Math.max(16, Math.round(this.cssW / 6));
    var sh = Math.max(16, Math.round(this.cssH / 6));
    var k = this.wake;
    if (sw !== k.w || sh !== k.h) {
      k.tex.forEach(function (t) { gl.deleteTexture(t); });
      k.fb.forEach(function (f) { gl.deleteFramebuffer(f); });
      var still = new Uint8Array(sw * sh * 4);
      for (var i = 0; i < still.length; i += 4) { still[i] = 128; still[i + 1] = 128; still[i + 3] = 255; }
      k.tex = [texture(gl, sw, sh, still), texture(gl, sw, sh, still)];
      k.fb = k.tex.map(function (t) {
        var fb = gl.createFramebuffer();
        gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
        gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0);
        return fb;
      });
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      k.w = sw;
      k.h = sh;
      k.i = 0;
    }
    if (this.static || !this.running) this.render();
  };

  // Where the pointer is, in page coordinates.
  GoldLiquid.prototype.poke = function (clientX, clientY) {
    var r = this.canvas.getBoundingClientRect();
    var x = clientX - r.left;
    var y = clientY - r.top;
    if (!this.ptr) {
      this.ptr = [x, y];
      this.sm = [x, y];
      this.prevSm = [x, y];
    }
    this.ptr[0] = x;
    this.ptr[1] = y;
    // The light leans only slightly toward the pointer; a big swing reads as a flat picture tilting.
    this.lightTarget[0] = -0.4 + (x / r.width - 0.5) * 0.35;
    this.lightTarget[1] = 0.6 - (y / r.height - 0.5) * 0.25;
  };

  // Mask mode: the liquid only shows where the source canvas has alpha.
  GoldLiquid.prototype.setMask = function (source) {
    if (!this.useMask) return;
    var gl = this.gl;
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.maskTex);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
    gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, source);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
    if (!this.running) this.render();
  };

  GoldLiquid.prototype.stepWake = function () {
    var gl = this.gl;
    var k = this.wake;
    var vx = 0;
    var vy = 0;
    var mx = -10;
    var my = -10;
    if (this.sm) {
      // Ease toward the pointer, then push the wake by how far the eased point moved this frame.
      this.sm[0] += (this.ptr[0] - this.sm[0]) * 0.3;
      this.sm[1] += (this.ptr[1] - this.sm[1]) * 0.3;
      var dx = this.sm[0] - this.prevSm[0];
      var dy = this.sm[1] - this.prevSm[1];
      this.prevSm[0] = this.sm[0];
      this.prevSm[1] = this.sm[1];
      this.vel[0] += (dx - this.vel[0]) * 0.5;
      this.vel[1] += (dy - this.vel[1]) * 0.5;
      vx = Math.max(-0.5, Math.min(0.5, this.vel[0] * 0.03));
      vy = Math.max(-0.5, Math.min(0.5, -this.vel[1] * 0.03));
      mx = this.sm[0] / this.cssW;
      my = 1 - this.sm[1] / this.cssH;
    }
    var s = this.sim;
    gl.useProgram(s.prog);
    gl.bindFramebuffer(gl.FRAMEBUFFER, k.fb[1 - k.i]);
    gl.viewport(0, 0, k.w, k.h);
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, k.tex[k.i]);
    gl.uniform1i(s.loc.uPrev, 1);
    gl.uniform2f(s.loc.uSimRes, k.w, k.h);
    gl.uniform2f(s.loc.uSize, this.cssW, this.cssH);
    gl.uniform2f(s.loc.uMouse, mx, my);
    gl.uniform2f(s.loc.uVel, vx, vy);
    gl.uniform1f(s.loc.uRadius, this.wakeRadius);
    gl.uniform1f(s.loc.uDecay, 0.975);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    k.i = 1 - k.i;
  };

  GoldLiquid.prototype.render = function () {
    if (this.lost) return;
    var gl = this.gl;
    var now = performance.now();
    var time = (now - this.t0) / 1000;
    var W = this.canvas.width;
    var H = this.canvas.height;
    var s = this.scale;

    // Keep an eye on frame time; if the machine struggles, draw fewer pixels.
    if (this.running && this.prevNow) {
      this.frames.push(now - this.prevNow);
      if (this.frames.length >= 50) {
        var avg = this.frames.reduce(function (a, b) { return a + b; }, 0) / this.frames.length;
        this.frames.length = 0;
        if (avg > 24 && this.quality > this.minQuality) {
          this.quality = Math.max(this.minQuality, this.quality * 0.8);
          this.resize();
        }
      }
    }
    this.prevNow = now;

    if (this.running) this.stepWake();

    this.light[0] += (this.lightTarget[0] - this.light[0]) * 0.03;
    this.light[1] += (this.lightTarget[1] - this.light[1]) * 0.03;

    var m = this.main;
    var a = this.arch;
    gl.useProgram(m.prog);
    gl.viewport(0, 0, W, H);
    gl.uniform2f(m.loc.uRes, W, H);
    gl.uniform1f(m.loc.uTime, time);
    gl.uniform1f(m.loc.uCool, this.cool);
    gl.uniform1f(m.loc.uZoom, this.zoom);
    gl.uniform1f(m.loc.uFill, this.fill);
    gl.uniform1f(m.loc.uBright, this.bright);
    gl.uniform1f(m.loc.uScale, s);
    gl.uniform4f(m.loc.uArch, a.left * s, (this.cssH - a.top - a.height) * s, a.width * s, a.height * s);
    gl.uniform2f(m.loc.uLight, this.light[0], this.light[1]);
    gl.uniform1f(m.loc.uWakeAmp, this.wakeAmp);
    gl.uniform1f(m.loc.uUseMask, this.useMask ? 1 : 0);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.maskTex);
    gl.uniform1i(m.loc.uMask, 0);
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, this.wake.tex[this.wake.i]);
    gl.uniform1i(m.loc.uWake, 1);
    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  };

  // Runs only while on screen and the tab is visible.
  GoldLiquid.prototype.update = function () {
    var should = !this.static && !this.lost && this.visible && !document.hidden;
    if (should && !this.running) {
      this.running = true;
      this.prevNow = 0;
      this.raf = requestAnimationFrame(this.loop);
    } else if (!should && this.running) {
      this.running = false;
      cancelAnimationFrame(this.raf);
    }
  };

  GoldLiquid.prototype.start = function () {
    this.update();
  };

  GoldLiquid.supported = function () {
    try {
      var c = document.createElement("canvas");
      var gl = c.getContext("webgl");
      if (gl && gl.getExtension("WEBGL_lose_context")) gl.getExtension("WEBGL_lose_context").loseContext();
      return Boolean(gl);
    } catch (e) {
      return false;
    }
  };

  window.GoldLiquid = GoldLiquid;
})();
