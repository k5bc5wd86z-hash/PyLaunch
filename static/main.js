// Mobil Menü ve İnteraktif Özellikler
document.addEventListener('DOMContentLoaded', () => {
    console.log("Flask Starter Kit yüklendi!");

    // Mobil menü toggle butonu için dinamik mantık
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Flash mesajlarının otomatik kaybolması
    const flashMessages = document.querySelectorAll('.flash-msg');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            });
        }, 4000);
    }
});