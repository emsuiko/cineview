$(function() {
    $('#view-switch').bootstrapToggle({
        on: '2D',
        off: '3D'
    });
    $('#view-switch').change(function() {
        var two_d = $(this).prop('checked');
        var pathname = window.location.pathname;
        if (!~pathname.indexOf('rows')) {
            var pathname = pathname.replace("/view/", "/rows/view/");
        }
        if (two_d) {
            var res = pathname.replace("view/3", "view/2");
        } else {
            var res = pathname.replace("view/2", "view/3");
        }
        $.ajax({
            url: res
        }).done(function(data){
            $("#rows").html(data);
        })
    })
});