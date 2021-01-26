$(document).ready(function(){
    $("#submit-button").click(function() {
        $("#header-img-old").addClass("rotated");
        $("#header-img-old").fadeTo(1000, 0);
        $("#header-img-baby").delay(1000).fadeTo(1000,1);

        setTimeout(function() {
            window.scrollBy(0,800);
        }, 1500);
    });

});