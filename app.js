var main = function() {
	$('.sql').hide();	
	$('.btn-info').click(function() {
	$('.sql').toggle();	
});

	$('.btn-menu').click(function() {
	$('.menu-items').toggle();	
});
}
$(document).ready(main);
