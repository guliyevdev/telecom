function xxl() {
    $(".categories-item").css("margin", "0 0 13px 0");
}
xxl();
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