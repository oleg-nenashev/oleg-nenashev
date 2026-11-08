// Filters the generated talks list by the "tag" URL parameter.
(function () {
  function init() {
    var sections = Array.prototype.slice.call(
      document.querySelectorAll(".md-content ul.talk-list")
    );
    if (!sections.length) {
      return;
    }

    sections.forEach(function (section) {
      var more = section.nextElementSibling;
      var button = more && more.classList.contains("talk-more") &&
        more.querySelector(".talk-more-toggle");
      if (button) {
        button.addEventListener("click", function () {
          var expanded = button.getAttribute("aria-expanded") !== "true";
          button.setAttribute("aria-expanded", String(expanded));
          button.textContent = expanded ? "Fewer talks" : "More talks";
          apply();
        });
      }
    });

    var bar = document.createElement("div");
    bar.className = "talk-filter";
    bar.hidden = true;
    var title = document.querySelector(".md-content h1");
    title.parentNode.insertBefore(bar, title.nextSibling);

    function currentTag() {
      return new URLSearchParams(window.location.search).get("tag");
    }

    function apply() {
      var tag = currentTag();
      sections.forEach(function (section) {
        var more = section.nextElementSibling;
        var button = more && more.classList.contains("talk-more") &&
          more.querySelector(".talk-more-toggle");
        var expanded = button && button.getAttribute("aria-expanded") === "true";
        var hasMatches = false;
        var hasCollapsedMatches = false;
        section.querySelectorAll("li.talk-item").forEach(function (li) {
          var tags = Array.prototype.map.call(
            li.querySelectorAll("a.talk-tag[data-tag]"),
            function (a) { return a.dataset.tag; }
          );
          var matches = !tag || tags.indexOf(tag) !== -1;
          var collapsed = li.hasAttribute("data-collapsed");
          hasMatches = hasMatches || matches;
          hasCollapsedMatches = hasCollapsedMatches || (matches && collapsed);
          li.hidden = !matches || (collapsed && !expanded);
        });
        section.hidden = !hasMatches;
        if (button) {
          more.hidden = !hasCollapsedMatches;
        }

        var preceding = section.previousElementSibling;
        while (preceding && preceding.tagName !== "H1" && preceding.tagName !== "H2" &&
               !preceding.classList.contains("talk-list")) {
          if (preceding.tagName === "BLOCKQUOTE") {
            preceding.hidden = !hasMatches;
          }
          preceding = preceding.previousElementSibling;
        }
        if (preceding && preceding.tagName === "H2") {
          preceding.hidden = !hasMatches;
        }
      });
      document.querySelectorAll(".md-content a.talk-tag").forEach(function (a) {
        a.classList.toggle("active", a.dataset.tag === tag);
      });

      if (tag) {
        bar.textContent = "Showing talks tagged ";
        var strong = document.createElement("strong");
        strong.textContent = tag;
        bar.appendChild(strong);
        bar.appendChild(document.createTextNode(" · "));
        var clear = document.createElement("a");
        clear.href = window.location.pathname;
        clear.textContent = "Show all talks";
        clear.addEventListener("click", function (e) {
          e.preventDefault();
          history.pushState(null, "", window.location.pathname);
          apply();
        });
        bar.appendChild(clear);
        bar.hidden = false;
      } else {
        bar.hidden = true;
      }
    }

    document.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest("a.talk-tag[data-tag]");
      if (!a || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) {
        return;
      }
      e.preventDefault();
      var open = a.closest("dialog");
      if (open && open.open) {
        open.close();
      }
      var url = window.location.pathname + "?tag=" + encodeURIComponent(a.dataset.tag);
      history.pushState(null, "", url);
      apply();
    });
    var cloud = document.querySelector(".talk-tag-cloud");
    var toggle = cloud && cloud.querySelector(".talk-tags-toggle");
    function setExpanded(expanded) {
      cloud.classList.toggle("expanded", expanded);
      toggle.setAttribute("aria-expanded", expanded);
      toggle.textContent = expanded ? "\u2212" : "+";
      toggle.title = expanded ? "Show fewer tags" : "Show all tags";
    }
    if (toggle) {
      toggle.addEventListener("click", function () {
        setExpanded(!cloud.classList.contains("expanded"));
      });
      var wanted = currentTag();
      if (wanted && cloud.querySelector('.talk-tag-extra[data-tag="' + CSS.escape(wanted) + '"]')) {
        setExpanded(true);
      }
    }
    window.addEventListener("popstate", apply);
    apply();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// Talk details popups
document.addEventListener("click", function (e) {
  var open = e.target.closest && e.target.closest("[data-talk-dialog]");
  if (open) {
    var dialog = document.getElementById(open.dataset.talkDialog);
    if (dialog && dialog.showModal) {
      dialog.showModal();
    }
    return;
  }
  if (e.target.closest && e.target.closest(".talk-dialog-close")) {
    e.target.closest("dialog").close();
    return;
  }
  if (e.target.tagName === "DIALOG" && e.target.classList.contains("talk-dialog")) {
    e.target.close();
  }
});
