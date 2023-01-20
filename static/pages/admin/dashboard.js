//loadScript("https://unpkg.com/leaflet@1.9.3/dist/leaflet.js");
console.log(' new 	map dynamically loaded..')
var map = L.map('map').setView([13.0707,77.79814], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
L.marker([13.0707,77.79814]).addTo(map)
    .bindPopup('SAM:23[+2] | MAM:67[-23]')
    .openPopup();
	
L.marker([13.0707,77.784826]).addTo(map)
    .bindPopup('SAM:21[+2] | MAM:34[-23]')
    .openPopup();
	