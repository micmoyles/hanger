var main = function() {
	$('.sql').hide();	
	$('.btn-sql').click(function() {
	$('.sql').toggle();	
});
	$('.addPlant').hide();	
	$('.btn-addPlant').click(function() {
	$('.addPlant').toggle();	
});
	$('.menu-extension').hide();	
	$('.extend-menu').click(function() {
	$('.menu-extension').toggle();	
});
}
$(document).ready(main);
