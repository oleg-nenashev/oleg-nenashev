// Filters the generated talks list by the "tag" URL parameter.
(function () {
  function init() {
    var list = Array.prototype.slice.call(
      document.querySelectorAll(".md-content li")
    ).filter(function (li) {
      return li.querySelector("a.talk-tag[data-tag]");
    });
    if (!list.length) {
      return;
    }

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
      list.forEach(function (li) {
        var tags = Array.prototype.map.call(
          li.querySelectorAll("a.talk-tag[data-tag]"),
          function (a) { return a.dataset.tag; }
        );
        li.hidden = !!tag && tags.indexOf(tag) === -1;
        Array.prototype.forEach.call(li.querySelectorAll("a.talk-tag"), function (a) {
          a.classList.toggle("active", a.dataset.tag === tag);
        });
      });

      document.querySelectorAll(".md-content h2").forEach(function (h) {
        var section = h.nextElementSibling;
        while (section && section.tagName !== "UL") {
          section = section.nextElementSibling;
        }
        if (section && section.querySelector("a.talk-tag[data-tag]")) {
          var empty = !section.querySelector("li:not([hidden])");
          h.hidden = empty;
          section.hidden = empty;
        }
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
      var url = window.location.pathname + "?tag=" + encodeURIComponent(a.dataset.tag);
      history.pushState(null, "", url);
      apply();
    });
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
