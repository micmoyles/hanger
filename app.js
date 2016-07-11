var main = function() {
	$('.sql').hide();	
	$('.btn-info').click(function() {
	$('.sql').toggle();	
});
	$('.menu-extension').hide();	
	$('.extend-menu').click(function() {
	$('.menu-extension').toggle();	
});
}
$(document).ready(main);
