// buradaki kod django recursiv funksiyalarin getirdiyi childrenleri dizayn elemek ucundu
function start_css() {
    $(".categories-item").css("margin", "0 0 13px 0");
}
start_css();
$(".filter_Collapse").click(function(e) {
    var element = $(this).attr("class");
    if (element == "fi_title filter_Collapse") {
        $(this).addClass("active");
        $("#list-" + e.target.id).css("display", "block");
    } else {
        $(this).removeClass("active");
        $("#list-" + e.target.id).css("display", "none");
    }
});
// navbar
$(".toggler").click(function(e) {
    var element = $(this).attr("class");
    if (element == "toggler") {
        $(this).addClass("active active_second active_last");
        $('.h_bottom').addClass("show_me");
    } else {
        $(this).removeClass("active active active_second active_last");
        $('.h_bottom').removeClass("show_me");
    }
});
// filter
$(".filters_toggle").click(function(e) {
    var element = $(this).attr("class");
    if (element == "filters_toggle") {
        $(this).addClass("active");
        $('.filter_col').addClass("show_me");
    } else {
        $(this).removeClass("active");
        $('.filter_col').removeClass("show_me");
    }
});
// saerch
$(".search_open_close").click(function(e) {
    var element = $(this).attr("class");
    if (element == "htb_icon search search_open_close") {
        $('.search_pp').css("display", "block");
    } else {
        $('.search_pp').css("display", "none");
    }
});