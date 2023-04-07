// Top Scroll

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

// Navbar Feauture

function navbarMotion() {
  var element = $("#listaNav");
  var toogle = $("#menuToogle");

    element.toggleClass("hideNav");
    element.toggleClass("showNav");
    toogle.toggleClass("menuShow");
    toogle.toggleClass("menuHide");

}







