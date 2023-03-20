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

function showCartelera() {
  var ocultar = document.getElementById("ocultar");
  var element = document.getElementById("mostrar");
  var visualizar = document.getElementById("visualizar");

  element.classList.add("hero-cartelera-show");
  ocultar.classList.add("hide");
  visualizar.classList.remove("hide");
}

function showCarteleralg() {
  var ocultar = document.getElementById("ocultarlg");
  var element = document.getElementById("mostrar");
  var visualizar = document.getElementById("visualizarlg");

  element.classList.add("hero-cartelera-show");
  ocultar.classList.add("hide");
  visualizar.classList.remove("hide");
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



