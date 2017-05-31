function test(){

	$('#test').append('coucou  ');

	$('<div id="div1" class="col-md-12"/>').appendTo('body');

	$('<div id="div2" class="col-md-12" />').appendTo('body');

	$('#div1').append('test div 1');
	$('#div2').append('test div 2');
}
