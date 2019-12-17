$(window).scroll(() => {
    let scroll = $(window).scrollTop();
    if (scroll >= 550) {
        $("#mynav").addClass("bg-dark");
    } else {
        $("#mynav").removeClass("bg-dark");
    }
});