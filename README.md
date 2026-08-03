# PyLaunch
# 🚀 Modern Flask Portfolio & Starter Kit

Bu proje; geliştiriciler, ajanslar ve freelancerlar için özel olarak tasarlanmış, **Python Flask** ve **Tailwind CSS** tabanlı 5 sayfalık modern bir web şablonudur.
Projeyi bilgisayarınıza indirdikten sonra, terminalde açarak "pip install -r requirements.txt" yazmanız kurulum için yeterlidir, çalıştırmak için ise "python3 app.py" yazınız.

## 🛠️ Kullanılan Teknolojiler
* **Backend:** Python (Flask 3.0)
* **Frontend:** Tailwind CSS (CDN) + Özel CSS
* **İnteraktif Özellikler:** Vanilla JavaScript (Mobil menü & animasyonlar)
* **Şablon Motoru:** Jinja2

## 📁 Proje Mimarisi
```text
yeni_proje/
│
├── app.py                  # Ana Flask uygulama rotaları
├── requirements.txt        # Bağımlılıklar
├── static/
│   ├── css/style.css       # Özel stiller ve animasyonlar
│   └── js/main.js         # JavaScript işlevleri
└── templates/
    ├── base.html           # Ortak şablon (Navbar & Footer)
    ├── index.html          # Anasayfa (Terminal mockup)
    ├── about.html          # Hakkımda
    ├── services.html       # Hizmetler
    ├── projects.html       # Portfolyo (Psikoloji Havuzu Referansı)
    └── contact.html        # İletişim Formu & Flash Mesajlar
