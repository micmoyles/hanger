var main = function() {
	$('.sql').hide();	
	$('.btn-info').click(function() {
	$('.sql').toggle();	
});

	$('.btn-menu').click(function() {
	$('.menu-items').toggle();	
});
	$('.extend-menu').click(function() {
	$('.menu-extension').toggle();	
});
}
$(document).ready(main);
