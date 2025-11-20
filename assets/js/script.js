document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const contentWrapper = document.querySelector(".content-wrapper");
    const content = document.querySelector(".content");
    const menuToggle = document.getElementById("menu-toggle");
    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav-links");
    const backToTopButton = document.getElementById("backToTop");

    const loadBodyContent = () => {
        if (!contentWrapper || !content) return;
        const src = body.getAttribute("data-src");
        if (src) {
            contentWrapper.classList.add("loading");

            fetch(src)
                .then(response => {
                    if (!response.ok) throw new Error('Network response was not ok');
                    return response.text();
                })
                .then(data => {
                    content.innerHTML = data;
                    content.classList.add("loaded");
                    setTimeout(() => {
                        contentWrapper.classList.remove("loading");
                    }, 500);
                })
                .catch(error => {
                    console.error('There has been a problem with your fetch operation:', error);
                });
        }
    };

    if (contentWrapper && content) {
        window.addEventListener("scroll", () => {
            const scrollPosition = window.scrollY + window.innerHeight;
            if (scrollPosition >= document.body.offsetHeight) {
                loadBodyContent();
            }
        });
    }

    const syncNavState = () => {
        if (!menuToggle || !hamburger) return;
        const isOpen = menuToggle.checked;
        body.classList.toggle("nav-open", isOpen);
        hamburger.classList.toggle("is-active", isOpen);
        hamburger.setAttribute("aria-expanded", String(isOpen));
        if (navLinks) {
            navLinks.setAttribute("aria-hidden", String(!isOpen));
        }
    };

    if (menuToggle && hamburger) {
        menuToggle.addEventListener("change", syncNavState);
        if (navLinks) {
            navLinks.querySelectorAll("a").forEach(link => {
                link.addEventListener("click", () => {
                    if (menuToggle.checked) {
                        menuToggle.checked = false;
                        syncNavState();
                    }
                });
            });
        }
        syncNavState();
    }
    if (backToTopButton) {
        const toggleBackToTop = () => {
            if (window.scrollY > 400) {
                backToTopButton.classList.add("show");
            } else {
                backToTopButton.classList.remove("show");
            }
        };

        window.addEventListener("scroll", toggleBackToTop, { passive: true });
        toggleBackToTop();

        backToTopButton.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
});