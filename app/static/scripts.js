function getLocation() {
    if (navigator.geolocation) {
        return navigator.geolocation.getCurrentPosition(function(position){return position});
    } else {
        return 0;
    }
}

function myMap() {
var pos = getLocation();

if (pos == 0 || pos == undefined) {
    var myCenter = new google.maps.LatLng(51.4503269, -2.5938695);
}
else {
    var myCenter = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
}

var mapProp = {center:myCenter, zoom:12, scrollwheel:false, draggable:false, mapTypeId:google.maps.MapTypeId.ROADMAP};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
var marker = new google.maps.Marker({position:myCenter});
marker.setMap(map);
}