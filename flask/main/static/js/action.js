async function get_my_location() {
  var location_text = document.querySelector("#start_position_text").text;
  var startPos;
  var geoSuccess = function (position) {
    startPos = position;
    var lat = startPos.coords.latitude;
    var lon = startPos.coords.longitude;
    var start_posi_marker = make_marker(lat, lon);
    markers.push(start_posi_marker);
    showMarker(map, start_posi_marker);
    change_map_center(lat, lon);
  };
  navigator.geolocation.getCurrentPosition(geoSuccess);
}

function select_city() {
  var sido = document.querySelector("sido").value;
  var gu = document.querySelector("gugun").value;
  $.ajax({
    type: 'POST',
    url: '/search',
    data: {
      'sido': sido,
      'gu': gu
    },
    success: function (msg) {
      alert(msg);
    }
  });
}
// search function 
function search() {
  var dest_position = document.querySelector("#dest_position_text").value;
  if (!dest_position) {
    alert("please fill the blank below");
  }
  else {
    $.get('/search', { 'destination': dest_position }, function (data) {
      if (!data) {
        alert("there is no data!")
      }
      else {
        console.log(data);
      }
    });
  }
}

var get_my_location_btn = document.querySelector("#get_my_location_btn");
get_my_location_btn.addEventListener("click", get_my_location);
var search_location_btn = document.querySelector("#city_selection_btn")
search_location_btn.addEventListener("click", select_city);
var get_destination_btn = document.querySelector("#set_destination_btn");
get_destination_btn.addEventListener("click", search);

function edit_modal() {
  $.ajax({
    url: '/search',
    data: {
      id: $(elm).attr('data-id')
    },
    type: 'POST',
    success: function (res) {
      console.log(res);
    },
    error: function (error) {
      console.log(error);
    }
  });
}