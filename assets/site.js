/* Scarlet Rox concept site — shared behaviour.
   THE ONE SWAPPABLE CONSTANT: everything business-specific lives in SRX below.
   Change it once and the whole site updates. */
const SRX = {
  name: "Scarlet Rox Salon and Lash Works LLC",
  short: "Scarlet Rox",
  street: "63 East Center Street",
  city: "Moab",
  state: "UT",
  zip: "84532",
  phone: "+1 435-260-8732",
  phoneHref: "tel:+14352608732",
  area: "Moab, Utah"
};
document.documentElement.classList.add("js");

(function () {
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- inject the swappable constant into [data-srx] slots ---- */
  document.querySelectorAll("[data-srx]").forEach(function (el) {
    var key = el.getAttribute("data-srx");
    if (key === "phoneHref") { el.setAttribute("href", SRX.phoneHref); }
    else if (key === "fullAddress") { el.textContent = SRX.street + ", " + SRX.city + ", " + SRX.state + " " + SRX.zip; }
    else if (SRX[key] !== undefined) { el.textContent = SRX[key]; }
  });

  /* ---- mobile nav ---- */
  var burger = document.querySelector(".burger");
  var nav = document.querySelector(".nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (nav.classList.contains("open") && !nav.contains(e.target) && !burger.contains(e.target)) {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---- reveal on scroll (state machine, reduced-motion safe) ---- */
  var revealEls = document.querySelectorAll(".rv");
  if (revealEls.length && "IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- lookbook scrubber ---- */
  var stage = document.querySelector(".lb-stage");
  if (stage) {
    var track = stage.querySelector(".lb-track");
    var slides = track.querySelectorAll(".lb-slide");
    var dots = document.querySelectorAll(".lb-dots button");
    var count = document.querySelector(".lb-count");
    var idx = 0;
    function go(n) {
      idx = (n + slides.length) % slides.length;
      track.style.transform = "translateX(" + (-idx * 100) + "%)";
      dots.forEach(function (d, i) { d.setAttribute("aria-current", i === idx ? "true" : "false"); });
      if (count) count.textContent = "0" + (idx + 1) + " / 0" + slides.length;
      slides.forEach(function (s, i) { s.setAttribute("aria-hidden", i === idx ? "false" : "true"); });
    }
    document.querySelector(".lb-prev").addEventListener("click", function () { go(idx - 1); });
    document.querySelector(".lb-next").addEventListener("click", function () { go(idx + 1); });
    dots.forEach(function (d, i) { d.addEventListener("click", function () { go(i); }); });
    /* drag */
    var startX = 0, curX = 0, dragging = false;
    stage.addEventListener("pointerdown", function (e) {
      dragging = true; startX = e.clientX; curX = 0;
      track.classList.add("dragging");
      stage.setPointerCapture(e.pointerId);
    });
    stage.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      curX = e.clientX - startX;
      track.style.transform = "translateX(calc(" + (-idx * 100) + "% + " + curX + "px))";
    });
    function endDrag() {
      if (!dragging) return;
      dragging = false; track.classList.remove("dragging");
      if (curX < -60) go(idx + 1); else if (curX > 60) go(idx - 1); else go(idx);
    }
    stage.addEventListener("pointerup", endDrag);
    stage.addEventListener("pointercancel", endDrag);
    document.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight" && stage.contains(document.activeElement)) go(idx + 1);
      if (e.key === "ArrowLeft" && stage.contains(document.activeElement)) go(idx - 1);
    });
    go(0);
  }

  /* ---- accordion ---- */
  document.querySelectorAll(".acc-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      btn.setAttribute("aria-expanded", open ? "false" : "true");
      panel.style.maxHeight = open ? "0px" : panel.scrollHeight + "px";
    });
  });

  /* ---- gallery filters ---- */
  var filterBtns = document.querySelectorAll(".gal-filters button");
  if (filterBtns.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
        btn.setAttribute("aria-pressed", "true");
        var cat = btn.getAttribute("data-cat");
        document.querySelectorAll(".gal-grid figure").forEach(function (fig) {
          var show = cat === "all" || fig.getAttribute("data-cat") === cat;
          fig.classList.toggle("hide", !show);
        });
      });
    });
  }

  /* ---- booking form: validate, then honest demo state ---- */
  var form = document.getElementById("bookform");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[data-need]").forEach(function (input) {
        var field = input.closest(".field");
        var bad = !input.value.trim() || (input.type === "checkbox" && !input.checked);
        field.classList.toggle("invalid", bad);
        if (bad) ok = false;
      });
      var email = form.querySelector('input[type="email"]');
      if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        email.closest(".field").classList.add("invalid"); ok = false;
      }
      if (!ok) {
        var firstBad = form.querySelector(".field.invalid input, .field.invalid select, .field.invalid textarea");
        if (firstBad) firstBad.focus();
        return;
      }
      form.style.display = "none";
      document.getElementById("bookok").classList.add("show");
      document.getElementById("bookok").setAttribute("tabindex", "-1");
      document.getElementById("bookok").focus({ preventScroll: false });
    });
    form.querySelectorAll("[data-need]").forEach(function (input) {
      input.addEventListener("input", function () {
        input.closest(".field").classList.remove("invalid");
      });
    });
  }

  /* ---- cookie consent (this concept site sets no cookies of its own) ---- */
  var bar = document.getElementById("cookiebar");
  if (bar && !localStorage.getItem("srx-cookie-choice")) {
    bar.classList.add("show");
  }
  var accept = document.getElementById("cookie-accept");
  var decline = document.getElementById("cookie-decline");
  function choose(v) {
    try { localStorage.setItem("srx-cookie-choice", v); } catch (e) {}
    bar.classList.remove("show");
  }
  if (accept) accept.addEventListener("click", function () { choose("accepted"); });
  if (decline) decline.addEventListener("click", function () { choose("declined"); });
})();
