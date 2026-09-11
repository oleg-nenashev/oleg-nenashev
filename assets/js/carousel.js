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
        
        // Large hat graphic sitting on top of head profile image
        const mainHatSvg = document.getElementById("mainHeadHatSvg");
        const hatBrim = mainHatSvg ? mainHatSvg.querySelector(".hat-brim") : null;
        const hatCrown = mainHatSvg ? mainHatSvg.querySelector(".hat-crown") : null;
        const hatRibbon = mainHatSvg ? mainHatSvg.querySelector(".hat-ribbon") : null;

        // Colors for each hat index
        const hatStyles = [
            { brim: "#1d4ed8", crown: "#3b82f6", ribbon: "#60a5fa" }, // 0: Tools Engineer (Blue)
            { brim: "#c2410c", crown: "#f97316", ribbon: "#fb923c" }, // 1: Community Builder (Amber)
            { brim: "#4338ca", crown: "#6366f1", ribbon: "#818cf8" }, // 2: Project Lead (Indigo)
            { brim: "#6b21a8", crown: "#a855f7", ribbon: "#c084fc" }, // 3: DevRel (Purple)
            { brim: "#047857", crown: "#10b981", ribbon: "#34d399" }  // 4: Consultant (Emerald)
        ];

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

            // Update large hat sitting on head avatar
            if (mainHatSvg && hatStyles[currentHatIndex]) {
                const style = hatStyles[currentHatIndex];
                if (hatBrim) hatBrim.setAttribute("fill", style.brim);
                if (hatCrown) hatCrown.setAttribute("fill", style.crown);
                if (hatRibbon) hatRibbon.setAttribute("fill", style.ribbon);

                // Trigger pop placement animation
                mainHatSvg.classList.remove("hat-pop");
                void mainHatSvg.offsetWidth; // Force DOM reflow
                mainHatSvg.classList.add("hat-pop");
            }
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
