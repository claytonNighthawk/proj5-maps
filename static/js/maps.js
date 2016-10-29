function initMap() {
	var eugene = {lat: 44.0519, lng: -123.0867};
	var map = new google.maps.Map(document.getElementById('map'), { zoom: 13, center: eugene});

	google.maps.event.addListener(map, 'click', function(event) {
	placeMarker(event.latLng); 
	});
	placeMarker(eugene);
	
	var locations = {{ locations|safe }};
	for (i = 0; i < locations.length; i++) {
		placeMarker(locations[i]);
	}

	function placeMarker(location) {
		var infowindow = new google.maps.InfoWindow();
		var geocoder = new google.maps.Geocoder;
		geocoder.geocode({'location': location}, function(results, status) {
			infowindow.setContent(results[0].formatted_address);
		});
		var marker = new google.maps.Marker({position: location, map: map });
		marker.addListener('click', function() {
			infowindow.open(map, marker);
		});
	}
}