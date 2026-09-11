document.addEventListener("DOMContentLoaded", function () {
    initHatSelector();
});

if (typeof location$ !== "undefined") {
    location$.subscribe(function () {
        setTimeout(initHatSelector, 100);
    });
}

function initHatSelector() {
    const selectorContainers = document.querySelectorAll(".hat-selector-container");
    
    selectorContainers.forEach(function (container) {
        if (container.dataset.hatSelectorInitialized) return;
        container.dataset.hatSelectorInitialized = "true";

        const hatCards = Array.from(container.querySelectorAll(".hat-card"));
        const prevBtn = container.querySelector(".hat-nav-btn.prev");
        const nextBtn = container.querySelector(".hat-nav-btn.next");
        
        // Locate the matching details container
        const detailsContainer = document.querySelector(".hat-details-container");
        if (!detailsContainer || hatCards.length === 0) return;

        const detailPanels = Array.from(detailsContainer.querySelectorAll(".hat-details-panel"));

        let currentHatIndex = 0;

        function selectHat(index) {
            if (index < 0) index = hatCards.length - 1;
            if (index >= hatCards.length) index = 0;
            currentHatIndex = index;

            hatCards.forEach((card, i) => {
                const isActive = i === currentHatIndex;
                card.classList.toggle("active", isActive);
                card.setAttribute("aria-selected", isActive ? "true" : "false");
            });

            detailPanels.forEach((panel, i) => {
                const isActive = i === currentHatIndex;
                panel.classList.toggle("active", isActive);
            });
        }

        hatCards.forEach((card, i) => {
            card.addEventListener("click", function () {
                selectHat(i);
            });
        });

        if (prevBtn) {
            prevBtn.addEventListener("click", function () {
                selectHat(currentHatIndex - 1);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener("click", function () {
                selectHat(currentHatIndex + 1);
            });
        }

        // Initialize active state
        selectHat(0);
    });
}
