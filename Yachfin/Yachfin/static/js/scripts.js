    function initMap() {
    const location = { lat: 35.5547686, lng: 6.1507544 };
    const map = new google.maps.Map(document.getElementById("google-map"), {
        zoom: 15,
        center: location,
        styles: [
            { elementType: 'geometry', stylers: [{color: '#f5f5f5'}] },
            { elementType: 'labels.text.fill', stylers: [{color: '#616161'}] },
            { elementType: 'labels.text.stroke', stylers: [{color: '#f5f5f5'}] },
            { featureType: 'water', elementType: 'geometry', stylers: [{color: '#c9c9c9'}] }
        ]
    });

    const marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "Our Location"
    });
    }
    document.addEventListener('DOMContentLoaded', () => {
    
    /* --- 1. Mobile Menu Toggle --- */
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mainNav = document.getElementById('main-nav');

    if(mobileBtn) {
        mobileBtn.addEventListener('click', () => {
            mainNav.classList.toggle('mobile-active');
            
            // Toggle icon between bars and times
            const icon = mobileBtn.querySelector('i');
            if(mainNav.classList.contains('mobile-active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    /* --- 2. Before/After Slider Logic --- */
    const sliders = [
        { range: 'slider-range', before: 'before-layer', handle: 'slider-handle' },
        { range: 'slider-range1', before: 'before-layer1', handle: 'slider-handle1' },
        { range: 'slider-range2', before: 'before-layer2', handle: 'slider-handle2' },
    ];

    sliders.forEach(slider => {
        const range = document.getElementById(slider.range);
        const before = document.getElementById(slider.before);
        const handle = document.getElementById(slider.handle);

        if (range && before && handle) {
            range.addEventListener('input', (e) => {
                const value = e.target.value;

                // Reveal before image
                before.style.clipPath = `inset(0 ${100 - value}% 0 0)`;

                // Move the slider handle
                handle.style.left = `${value}%`;
            });
        }
    });



    /* --- 3. Modal Logic --- */
    const modal = document.getElementById('reservation-modal');
    const bookBtn = document.getElementById('book-now-btn');
    const closeModal = document.getElementById('close-modal');
    const heroBookBtn = document.getElementById('hero-book-now-btn');
    const navBookBtn = document.getElementById ('nav-book-now-btn');

    // Open Modal
    if(bookBtn && modal) {
        bookBtn.addEventListener('click', () => {
            modal.style.display = 'flex';
            // slight delay to allow display:flex to apply before adding class for transition
            setTimeout(() => {
                modal.classList.add('open');
            }, 10);
        });
    }
    
    if(heroBookBtn && modal) {
        heroBookBtn.addEventListener('click', () => {
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.classList.add('open');
            }, 10);
        });
    }

    if(navBookBtn && modal) {
        navBookBtn.addEventListener('click', () => {
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.classList.add('open');
            }, 10);
        });
    }



    // Close Modal Function
    const closeModalFunc = () => {
        if(modal) {
            modal.classList.remove('open');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300); // Wait for transition
        }
    };

    if(closeModal) {
        closeModal.addEventListener('click', closeModalFunc);
    }

    // Close when clicking outside content
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModalFunc();
        }
    });
    /* --- 5. Smooth Scroll for Anchor Links --- */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                // Close mobile menu if open
                if(mainNav.classList.contains('mobile-active')) {
                    mainNav.classList.remove('mobile-active');
                    mobileBtn.querySelector('i').classList.remove('fa-times');
                    mobileBtn.querySelector('i').classList.add('fa-bars');
                }

                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    const navbar = document.querySelector('.nav-bar-wrapper');
    const hero = document.querySelector('#hero');
    const mobileNav = document.getElementById('main-nav'); // your dropdown

    if(navbar && hero && mobileNav) {
        window.addEventListener('scroll', () => {
            if(window.scrollY > hero.offsetHeight) {
                navbar.classList.add('scrolled');
                mobileNav.classList.add('scrolled-bg'); // add your new style
            } else {
                navbar.classList.remove('scrolled');
                mobileNav.classList.remove('scrolled-bg'); // revert to original
            }
        });
    }
    
});
