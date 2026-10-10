from build import page
from home_page import home_body

page(
    "index.html",
    "KLS | Kejuruteraan Elektrik & Interkoneksi Tenaga Boleh Diperbaharui, Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS) telah beroperasi sebagai kontraktor kejuruteraan elektrik Kelas A, CIDB G7 dan pakar interkoneksi tenaga boleh diperbaharui di Malaysia sejak 1984.",
    home_body("ms"),
    scripts='<script src="../assets/js/entrance.js"></script>\n<script src="../assets/js/gallery.js"></script>\n',
    lang="ms",
    alt_url="https://www.klseri.com.my/index.html",
)
