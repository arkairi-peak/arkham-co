/* ==========================================================================
   KLS structured data
   Sourced from the current klseri.com.my (Home, Company Overview, Our People,
   Our Services, Key Projects, Certifications & Licenses, Careers, Contact).
   Only facts published on the source site are included here, nothing here
   is invented. Image paths point at the original site's media library;
   replace /assets/img/people/*.jpg and /assets/img/certs/*.png with your own
   locally-hosted copies before deploying (see README.md).
   ========================================================================== */

const KLS_PEOPLE = [
  {
    id: "lim-cheng-lai",
    name: "Lim Cheng Lai",
    role: "Founder",
    group: "Founder & Leadership",
    image: "https://www.klseri.com.my/wp-content/uploads/2021/02/Lim-Cheng-Lai.jpg",
    initials: "LCL",
    bio: "Lim Cheng Lai is the founder of KLS and is the key person who led and transformed the company from a humble electrical motor wiring workshop into an established Class A, CIDB G7 M&E Contractor. He sets the direction of the company and leads the charge of a young and dynamic technical team.",
    facts: [
      ["Certification", "B4 33KV Chargeman (Energy Commission)"],
      ["Certification", "PW4 Wireman (Energy Commission)"],
      ["Focus", "Company direction & technical leadership"]
    ]
  },
  {
    id: "tengku-dato-ardy",
    name: "YDM Tengku Dato' Ardy Esfandiari Bin Tengku Hamid Shah Al Haj Tengku Seri Paduka Shahbandar (Selangor)",
    shortName: "YDM Tengku Dato' Ardy Esfandiari",
    role: "Founder",
    group: "Founder & Leadership",
    image: "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-03-797x1024.jpg",
    initials: "TA",
    bio: "One of the founders of KLS, YDM Tengku Dato' Ardy is instrumental in the company's public and government affairs liaison department. An established entrepreneur with extensive networking and excellent public relations skills, he helped build KLS into a company reputable amongst Government Linked Companies.",
    facts: [
      ["Honour", "Darjah Kebesaran Dato' Sultan Sharafudin Idris Shah (D.S.I.S), conferred 2012, for the 67th birthday of the Sultan of Selangor"],
      ["Board Position", "CB Industrial Products Bhd."],
      ["Focus", "Public affairs & government affairs liaison"]
    ]
  },
  {
    id: "ir-lim-yee-chard",
    name: "Ir. Lim Yee Chard",
    role: "Technical Leadership",
    group: "Technical Leadership",
    image: "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-02-796x1024.jpg",
    initials: "LYC",
    bio: "Ir. Lim currently oversees all projects undertaken by KLS. As a practising Professional Engineer and registered ASEAN Engineer, he is responsible for the overall tendering, execution and handing over of all major projects, leading an energetic and dedicated technical team to ensure projects are completed exceeding expectations and within budget.",
    facts: [
      ["Education", "UMIST (University of Manchester Institute of Science and Technology), UK, graduated 2002"],
      ["Registration", "Practising Professional Engineer"],
      ["Registration", "Registered ASEAN Engineer"],
      ["Responsibility", "Tendering, execution and handover of major projects"]
    ]
  },
  {
    id: "ir-jeremy-goh",
    name: "Ir. Jeremy Goh Jing Wei",
    role: "Technical Leadership",
    group: "Technical Leadership",
    image: "https://www.klseri.com.my/wp-content/uploads/2021/02/Jeremy.jpg",
    initials: "JG",
    bio: "Ir. Jeremy Goh joined KLS in 2014 and is the head engineer responsible for the technical and authorities liaison aspect of all KLS projects. An experienced and technical engineer, he has a proven track record in managing projects.",
    facts: [
      ["Education", "UniTEN (Universiti Tenaga Nasional), Degree in Electrical and Electronics Engineering (Hons.), 2013"],
      ["Registration", "Registered Professional Engineer"],
      ["Joined KLS", "2014"],
      ["Responsibility", "Technical & authorities liaison, head engineer"]
    ]
  },
  {
    id: "ali-naazzam",
    name: "Ali Na'Azzam",
    role: "Business Development",
    group: "Business Development",
    image: "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-01-796x1024.jpg",
    initials: "AN",
    bio: "Ali Na'Azzam is responsible for the business development of KLS. Equipped with strong PR skills and a vast network circle, he is also well versed in the construction industry with more than 25 years of experience.",
    facts: [
      ["Education", "Bachelor of Law (LLB)"],
      ["Experience", "25+ years in the construction industry"],
      ["Position", "Nominated as Executive Director since 2018"],
      ["Responsibility", "Business development"]
    ]
  }
];

/* Project reference list, exactly as published under "Key Projects" /
   "Project Reference List". category used for filtering:
   power = electrical power distribution / general M&E
   biogas / biomass / solar = renewable energy interconnection */
const KLS_PROJECTS = [
  { client:"FELDA Global Venture Holdings Berhad", short:"FELDA", entries:[
    { desc:"Mechanical & Electrical works for power generation plant (DP2B) at MSM Sugar Refinery (Johor) Sdn Bhd", year:2016, location:"Johor", category:"power" },
    { desc:"Electrical works for Kilang Baja FPM, Kuantan, Pahang", year:2016, location:"Kuantan, Pahang", category:"power" },
    { desc:"1600kW genset & electrical works at Sahabat Oil Products", year:2017, location:"Lahad Datu, Sabah", category:"power" }
  ]},
  { client:"Sime Darby Berhad", short:"Sime Darby", entries:[
    { desc:"Mechanical & Electrical works at Sime Darby Biodiesel Sdn Bhd", year:2016, location:"Carey Island, Selangor", category:"power" },
    { desc:"Electrical Interconnection works for proposed 1.6MW Biogas at Tennamaram POM", year:2017, location:"Bestari Jaya, Selangor", category:"biogas", capacity:"1.6MW" }
  ]},
  { client:"Top Glove Corporation Berhad", short:"Top Glove", entries:[
    { desc:"Electrical work for Factory 24 & 25", year:2011, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory 26", year:2012, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory 29", year:2013, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for 33kV SSU", year:2014, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory 30", year:2015, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory 32", year:2017, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory F2B", year:2019, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory F40", year:2019, location:"Klang Utara, Mukim Kapar, Klang", category:"power" },
    { desc:"Electrical work for Factory F20A", year:2020, location:"Klang Utara, Mukim Kapar, Klang", category:"power" }
  ]},
  { client:"Cenergi EPC Sdn. Bhd.", short:"Cenergi EPC", entries:[
    { desc:"Electrical Interconnection works for 1.5MW Biogas at Kilang Sawit Jelutung", year:2016, location:"Pahang", category:"biogas", capacity:"1.5MW" },
    { desc:"Electrical Interconnection works for 1.5MW Biogas at Pantai Remis Palm Oil Mill", year:2018, location:"Perak", category:"biogas", capacity:"1.5MW" },
    { desc:"Electrical Interconnection works for 1.5MW Biogas at Kilang Sawit Felcra Jayaputra", year:2019, location:"Pahang", category:"biogas", capacity:"1.5MW" },
    { desc:"Electrical Interconnection works for 2.0MW Biogas at Sri Ganda Oil Mill", year:2020, location:"Perak", category:"biogas", capacity:"2.0MW" },
    { desc:"Electrical works of 11kV overhead cable (15.0km) at Sri Ganda Oil Mill", year:2020, location:"Perak", category:"power" }
  ]},
  { client:"Sabah Electricity Sdn. Bhd. (SESB)", short:"SESB", entries:[
    { desc:"T7408 – Remote Terminal Unit Electrical works for Eastern Region Power Station & Distribution Substation", year:2016, location:"Sabah", category:"power" }
  ]},
  { client:"Telekom Malaysia Berhad", short:"Telekom Malaysia", entries:[
    { desc:"Electrical upgrading works for TM Jalan Raja Chulan, TM Kelana Jaya and Menara TM", year:2013, location:"Kuala Lumpur / Selangor", category:"power" }
  ]},
  { client:"KLK Berhad", short:"KLK Berhad", entries:[
    { desc:"Electrical works for Stolthaven Phase 10", year:2019, location:"Westport", category:"power" },
    { desc:"Electrical works for 6.5MW GTG COGEN at Palm Oleo Rawang", year:2020, location:"Rawang, Selangor", category:"power", capacity:"6.5MW" }
  ]},
  { client:"Worldwide Holdings Berhad", short:"Worldwide Holdings", entries:[
    { desc:"Electrical Interconnection works for 3MW Biogas at Jeram Sanitary Landfill", year:2020, location:"Kuala Selangor", category:"biogas", capacity:"3MW" }
  ]},
  { client:"Cepat Wawasan Group Berhad", short:"Cepat Wawasan", entries:[
    { desc:"Electrical Interconnection works for 10MW Biomass at Prolific Yield Oil Mill", year:2011, location:"Sandakan", category:"biomass", capacity:"10MW" },
    { desc:"Electrical Interconnection works for 3.5MW Biogas at Mistral Engineering", year:2015, location:"Sandakan", category:"biogas", capacity:"3.5MW" }
  ]},
  { client:"North Port Malaysia", short:"North Port", entries:[
    { desc:"Upgrading of existing old 11kV switchgear at Substation 23, CT2", year:2019, location:"Port Klang, Selangor", category:"power" },
    { desc:"Replacement of 11kV for Substation No.8, CT1", year:2020, location:"Port Klang, Selangor", category:"power" }
  ]},
  { client:"Cargill Palm Products Sdn Bhd", short:"Cargill", entries:[
    { desc:"Mechanical, Electrical & ELV works for new refinery at Lot 69894 PKFZ", year:2014, location:"Port Klang, Selangor", category:"power" },
    { desc:"Electrical work for new refinery (Rubik 1), Jalan Kem", year:2020, location:"Port Klang, Selangor", category:"power" }
  ]},
  { client:"Dialog Group Berhad", short:"Dialog Group", entries:[
    { desc:"Electrical works for EPCC Marine Facilities (Jetty 3), Pengerang Deep Water Terminal Phase-3 Development (PENTA-OCEAN)", year:2020, location:"Pengerang, Johor", category:"power" },
    { desc:"Electrical works for Deep Water Terminal Project Marine Facilities (Jetty 2) inner & outer arm jetty monitoring building (PENTA-OCEAN)", year:2020, location:"Pengerang, Johor", category:"power" }
  ]},
  { client:"United Plantations Berhad", short:"United Plantations", entries:[
    { desc:"Electrical works for proposed Palm Oil Mill, Refinery (PRIME) and biogas interconnection", year:2017, location:"Ulu Bernam", category:"biogas" },
    { desc:"Electrical works for Unifractions", year:2018, location:"Ulu Bernam", category:"power" }
  ]}
];

/* Featured / highlighted clients from the "Key Projects" section */
const KLS_FEATURED_CLIENTS = [
  "Top Glove Berhad","Cenergi SEA Sdn. Bhd.","Telekom Malaysia Berhad","Sime Darby Berhad",
  "Cepat Wawasan Sdn. Bhd.","KLK Berhad","Cargill Palm Products Sdn. Bhd."
];

/* Key Clients logo/name grid (as listed on the homepage) */
const KLS_KEY_CLIENTS = [
  { name:"KL-Kepong Oleomas", url:"https://www.klkoleo.com/", logo:"assets/img/clients/klk-oleo.png" },
  { name:"Northport Malaysia", url:"https://www.northport.com.my/npv2/index.html", logo:"assets/img/clients/northport.png" },
  { name:"Sabah Electricity (SESB)", url:"https://www.sesb.com.my/", logo:"assets/img/clients/sabah-electricity.png" },
  { name:"Sime Darby Berhad", url:"https://www.simedarby.com/", logo:"assets/img/clients/sime-darby.png" },
  { name:"Telekom Malaysia", url:"https://www.tm.com.my/Pages/Home.aspx", logo:"assets/img/clients/telekom-malaysia.png" },
  { name:"Cargill Malaysia", url:"https://www.cargill.com.my/", logo:"assets/img/clients/cargill.png" },
  { name:"Cenergi SEA", url:"https://www.cenergi-sea.com/", logo:"assets/img/clients/cenergi.png" },
  { name:"Cepat Group", url:"http://cepatgroup.com/", logo:"assets/img/clients/cepat-wawasan.png" },
  { name:"FELCRA Berhad", url:"https://felcra.com.my/", logo:"assets/img/clients/felcra.png" },
  { name:"FGV Holdings", url:"https://www.fgvholdings.com/home/", logo:"assets/img/clients/fgv-holdings.png" },
  { name:"Hap Seng", url:"https://www.hapseng.com.my/en/", logo:"assets/img/clients/hap-seng.png" }
];

/* Partners & Suppliers, as listed on the homepage */
const KLS_PARTNERS = [
  { name:"Viscon", url:"http://www.viscon.com.my/", logo:"assets/img/partners/viscon.png" },
  { name:"INNIO Jenbacher", url:"https://www.innio.com/en/products/jenbacher", logo:"assets/img/partners/innio-jenbacher.png" },
  { name:"Grid Vision T&D", url:"https://www.gridvisiontnd.com/", logo:"assets/img/partners/grid-vision.png" },
  { name:"SP Nergy", url:"http://www.spnergy.com/", logo:"assets/img/partners/sp-nergy.png" },
  { name:"OSK Group", url:"https://www.oskgroup.com/", logo:"assets/img/partners/osk-group.png" },
  { name:"Schneider Electric", url:"https://www.se.com/my/en/", logo:"assets/img/partners/schneider-electric.png" },
  { name:"Terasaki", url:"https://www.terasaki.com.my/", logo:"assets/img/partners/terasaki.png" },
  { name:"ABB", url:"https://new.abb.com/my", logo:"assets/img/partners/abb.png" },
  { name:"Fuji Electric", url:"https://www.fujielectric.com/", logo:"assets/img/partners/fuji-electric.png" },
  { name:"Tamco", url:"https://www.tamco.com.my/", logo:"assets/img/partners/tamco.png" },
  { name:"Ekarat", url:"https://www.ekarat.co.th/en/home/", logo:"assets/img/partners/ekarat.png" },
  { name:"Sime Darby Berhad", url:"https://www.simedarby.com/", logo:"assets/img/clients/sime-darby.png" }
];

/* Advisors & Consultants, as listed on the homepage */
const KLS_ADVISORS = [
  { name:"ZP", url:"https://www.zp.com.my/", logo:"assets/img/partners/zp.png" },
  { name:"Sistem Konsult", url:"https://sistemkonsult.com.my/", logo:"assets/img/partners/sistem-konsult.png" },
  { name:"Malim", url:"https://www.malim.com.my/", logo:"assets/img/partners/malim.png" },
  { name:"Duriane", url:"http://www.duriane.com/", logo:"assets/img/partners/duriane.png" },
  { name:"UPC", url:"https://upc.com.my/", logo:"assets/img/partners/upc.png" }
];

/* Certifications & Licenses, the source page displays 12 certificate /
   licence images without individual captions; presented here as a numbered
   set matching the order on klseri.com.my/certifications-licenses/ */
const KLS_CERTS = Array.from({length:12}, (_,i)=>({
  n: i+1,
  image: `https://www.klseri.com.my/wp-content/uploads/2021/02/${i+1}.png`
}));
