site_url = "shoten.gg"
local_url = "http://127.0.0.1:8000"
$(document).on("submit", "#post-form", function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/create",
        data: {
            link: $("#link").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function (data) {
            $("h2").html(site_url + "/" + data);
        },
    });
});