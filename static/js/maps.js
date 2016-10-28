function initMap() {
	var eugene = {lat: 44.0519, lng: -123.0867};
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 13,
		center: eugene
	});
	var marker = new google.maps.Marker({
		position: eugene,
		map: map
	});
	
	google.maps.event.addListener(map, 'click', function(event) {
	 placeMarker(event.latLng);
});

	function placeMarker(location) {
		var infowindow = new google.maps.InfoWindow({
		});

		

		var marker = new google.maps.Marker({
				position: location, 
				map: map
		});
		marker.addListener('click', function() {
    	infowindow.open(map, marker);
  		});
	}
}