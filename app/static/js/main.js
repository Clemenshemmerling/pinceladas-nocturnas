/*$(document).ready(function() {

    $(document)[0].oncontextmenu = function() { return false; }

    $(document).mousedown(function(e) {
        if( e.button == 2 ) {
            alert('Perdona tienes que comprar la imagen para poder descargarla');
            return false;
        } else {
            return true;
        }
    });
});*/

/*$(document).ready(function(){
	$(".div-ctn").mouseover(function(){
		$(".div-p").show("blind");
	});
	$(".div-ctn").mouseleave(function(){
		$(".div-p").hide("blind");
	});
});*/
$(document).ready(function(){
	$(".menu").click(function(){
		$(".down-menu").toggle("drop", { direction: "left"}, 500);
	});
});