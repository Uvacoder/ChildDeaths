$(function() {
	$("#tab_area").load("tabs.html #tab_container");
	$("#modal").load("tabs.html #delayed-modal")
	$('#CFR_table').tablesorter({
		theme: 'blue',
		widgetOptions: {
			build_type   : 'json',
			build_source : { url: 'data/CFR_table.json', dataType: 'json' }
		}
	});
	$('#unreviewed_table').tablesorter({
		theme: 'blue',
		widgetOptions: {
			build_type   : 'json',
			build_source : { url: 'data/unreviewed_table.json', dataType: 'json' }
		}
	});
});