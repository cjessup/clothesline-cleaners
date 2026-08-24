(function () {
  "use strict";

  var yearEls = document.querySelectorAll("[data-year]");
  var thisYear = String(new Date().getFullYear());
  yearEls.forEach(function (el) { el.textContent = thisYear; });

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
      });
    });
  }

  var sheet = document.getElementById("call-sheet");
  document.querySelectorAll("[data-open-call]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (sheet && typeof sheet.showModal === "function") sheet.showModal();
    });
  });

  function boiseNow() {
    var parts = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/Boise",
      weekday: "short",
      hour: "numeric",
      minute: "numeric",
      hour12: false
    }).formatToParts(new Date());
    var map = {};
    parts.forEach(function (p) { map[p.type] = p.value; });
    var hour = Number(map.hour === "24" ? "0" : map.hour);
    return { weekday: map.weekday, minutes: hour * 60 + Number(map.minute) };
  }

  function windowFor(day, closeThu) {
    if (day === "Sun") return null;
    if (day === "Sat") return { open: 9 * 60, close: 14 * 60, until: "2:00 PM" };
    if (day === "Fri") return { open: 8 * 60, close: 19 * 60, until: "7:00 PM" };
    return { open: 8 * 60, close: closeThu, until: closeThu === 17 * 60 + 30 ? "5:30 PM" : "5:00 PM" };
  }

  function labelFor(hours, now) {
    if (!hours) return { open: false, label: "Closed Sunday" };
    if (now.minutes >= hours.open && now.minutes < hours.close) {
      return { open: true, label: "Open now · until " + hours.until };
    }
    if (now.minutes < hours.open) return { open: false, label: "Opens today " + (now.weekday === "Sat" ? "9:00 AM" : "8:00 AM") };
    if (now.weekday === "Sat") return { open: false, label: "Closed · opens Monday 8:00 AM" };
    if (now.weekday === "Fri") return { open: false, label: "Closed · opens Saturday 9:00 AM" };
    return { open: false, label: "Closed · opens tomorrow 8:00 AM" };
  }

  var now = boiseNow();
  var orchard = labelFor(windowFor(now.weekday, 17 * 60), now);
  var meridian = orchard;
  var linder = labelFor(windowFor(now.weekday, 17 * 60 + 30), now);
  var anyOpen = orchard.open || linder.open;

  document.querySelectorAll("[data-open-status]").forEach(function (el) {
    var which = el.getAttribute("data-open-status");
    var st = which === "linder" ? linder : which === "any" ? (anyOpen ? orchard : linder) : orchard;
    if (which === "any") {
      el.textContent = anyOpen ? "Stores open now (Boise time)" : st.label;
      el.classList.toggle("is-open", anyOpen);
      el.classList.toggle("is-closed", !anyOpen);
    } else {
      el.textContent = st.label;
      el.classList.toggle("is-open", st.open);
      el.classList.toggle("is-closed", !st.open);
    }
  });
})();
