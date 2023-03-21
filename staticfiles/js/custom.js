var btn = $("#topscroll");

$(window).scroll(function () {
  if ($(window).scrollTop() > 300) {
    btn.addClass("show");
  } else {
    btn.removeClass("show");
  }
});

btn.on("click", function (e) {
  e.preventDefault();
  $("html, body").animate({ scrollTop: 0 }, "300");
});

function navbarMotion() {
  var element = $("#listaNav");
  var toogle = $("#menuToogle");

    element.toggleClass("hideNav");
    element.toggleClass("showNav");
    toogle.toggleClass("menuShow");
    toogle.toggleClass("menuHide");

}

var buton = $("#downarrow");

$(window).scroll(function () {
  if ($(window).scrollTop() > 1000) {
    buton.addClass("arrow-show");
  } else {
    buton.removeClass("arrow-show");
  }
});

buton.on("click", function (e) {
  e.preventDefault();
  $("html, body").animate({ scrollTop: $(document).height() }, "300");
});

// document.addEventListener("DOMContentLoaded", function () {
//   var calendarEl = document.getElementById("calendar");
//   var fechaInicial = Date.now();

//   var calendar = new FullCalendar.Calendar(calendarEl, {
//     initialView: "dayGridMonth",
//     initialDate: fechaInicial,
//     locale: "es",
//     buttonText: {
//       today: "HOY",
//     },
//     headerToolbar: {
//       left: "",
//       center: "title",
//       right: "today",
//     },
//     events: [
//       {
//         title: "{{obra.nombre}}",
//         start: "2022-06-25",
//         url: "{{evento.url}}",
//       },
//     ],
//   });

//   calendar.render();
// });



