menu = location.pathname;
if (menu == '/crypto/base-decode') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            $.post("/api/decode/base", {
                enc: $("#input").val()
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/crypto/base-encode') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var baseVal = $('input[name="base"]:checked').val();
            $.post("/api/encode/base", {
                plain: $("#input").val(),
                base: baseVal
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/hash/encrypt') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var hashVal = $('input[name="func"]:checked').val();
            $.post("/api/encrypt/hash", {
                plain: $("#input").val(),
                func: hashVal
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/hash/decrypt') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var hashVal = $('input[name="func"]:checked').val();
            $.post("/api/decrypt/hash", {
                hash: $("#input").val(), func: hashVal
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/web/post') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var funcVal = $('input[name="func"]:checked').val();
            $.post("/api/web/post", {
                url: $("#url").val(),
                json: $("#json-data").val(),
                data: $("#form-data").val()
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/pwnable/terminal') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var command = $("#input").val();
            $.post("/api/pwn/terminal", {
                cmd: command
            }, function (data) {
                $("#output").val(data);
            });
        });
    });
}
else if (menu == '/forensic/file-info') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var fDat = new FormData;
            fDat.append("file", $("input[name=file]")[0].files[0]);
            $.ajax({
                url: '/api/forensic/fileinfo',
                data: fDat,
                processData: false,
                contentType: false,
                type: 'POST',
                success: function (data) {
                    $("#output").val(data);
                }
            });
        });
    });
}
else if (menu == '/forensic/find-string') {
    $(document).ready(function () {
        $("#okBtn").click(function () {
            var fDat = new FormData;
            fDat.append("file", $("input[name=file]")[0].files[0]);
            fDat.append("regex", $("#input").val());
            $.ajax({
                url: '/api/forensic/findstring',
                data: fDat,
                processData: false,
                contentType: false,
                type: 'POST',
                success: function (data) {
                    $("#output").val(data);
                }
            });
        });
    });
}