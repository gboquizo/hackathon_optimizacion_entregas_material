


var map = L.map("map").setView([40.28, -3.7], 13);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let DefaultIcon = L.icon({
    iconUrl: 'static/img/marker-icon2.svg',
    // shadowUrl: iconShadow
});


L.Marker.prototype.options.icon = DefaultIcon;

L.Marker.prototype.options.icon = DefaultIcon;
map.on("contextmenu", function (event) {
  console.log("user right-clicked on map coordinates: " + event.latlng.toString());
  L.marker(event.latlng).addTo(map);
});
