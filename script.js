document.addEventListener("DOMContentLoaded", function () {
    const body = document.querySelector("body");
    const contentWrapper = document.querySelector(".content-wrapper");
    const content = document.querySelector(".content");

    const loadBodyContent = () => {
        const src = body.getAttribute("data-src");
        if (src) {
            // Show loading animation
            contentWrapper.classList.add("loading");

            fetch(src)
                .then(response => {
                    if (!response.ok) throw new Error('Network response was not ok');
                    return response.text();
                })
                .then(data => {
                    content.innerHTML = data; // Load the new content
                    content.classList.add("loaded"); // Fade in the new content
                    setTimeout(() => {
                        contentWrapper.classList.remove("loading"); // Remove loading animation after fade-in
                    }, 500); // Duration should match the animation
                })
                .catch(error => {
                    console.error('There has been a problem with your fetch operation:', error);
                });
        }
    };

    // Optionally observe the body or add a scroll event to load content
    window.addEventListener("scroll", () => {
        const scrollPosition = window.scrollY + window.innerHeight;
        if (scrollPosition >= document.body.offsetHeight) {
            loadBodyContent();
        }
    });
});