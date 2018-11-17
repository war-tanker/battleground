menu = location.pathname;
if (menu == '/crypto/base-decode/') {
    $.document.ready(function() {
        $("#okBtn").click(function() {
            $.post("/decode/base", {enc:$("#input").val()}, function(data) {
                $("#output").val(data);
            });
        });
    });
}