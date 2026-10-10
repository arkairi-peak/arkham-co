from build import page
from home_page import home_body

page(
    "index.html",
    "KLS | Electrical Engineering & Renewable Energy Interconnection, Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS) has operated as a Class A, CIDB G7 electrical engineering contractor and renewable energy interconnection specialist in Malaysia since 1984.",
    home_body("en"),
    scripts='<script src="assets/js/entrance.js"></script>\n<script src="assets/js/gallery.js"></script>\n',
    alt_url="https://www.klseri.com.my/ms/index.html",
)
