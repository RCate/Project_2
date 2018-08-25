// Creating map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Link to JSON files
var link1 = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json";
var link2 = "https://raw.githubusercontent.com/RCate/Project_2/master/Resources/Tuition/tuitionPercent.json";
var link3 = "https://raw.githubusercontent.com/RCate/Project_2/master/Code/4YrEnrollPctChange.json"

d3.queue()
  .defer(d3.json, link1)
  .defer(d3.json, link2)
  .defer(d3.json, link3)
  .await(ready);

function ready(error, mapData, csvData, csvData2) {
  if(error) return console.log(error);

  
  var csvData_obj = csvData.reduce(function(acc, data){
    acc[data.State] = data
    return acc
  },{})

  var csvData2_obj = csvData2.reduce(function(acc, data){
    acc[data.State] = data
    return acc
  },{})

  mapData.features.forEach(function(feature){
    feature.tuition = csvData_obj[feature.properties.name]
  })

  mapData.features.forEach(function(feature){
    feature.enrollment = csvData2_obj[feature.properties.name]
  })
  
   
  function onEachFeature(feature, layer) {
    if (feature.properties.name !== "Puerto Rico"){
      var tuition_pct_change = feature.tuition.Y2015 * 100;
      var enroll_pct_change = feature.enrollment.Y2015 * 100;
      layer.bindPopup("<h3>" + feature.properties.name +
        "</h3><hr><p>Tuition Change: " +  parseFloat(tuition_pct_change).toFixed(2) + "%</p>" +
        "</h3><hr><p>Enrollment Change: " + parseFloat(enroll_pct_change).toFixed(2) + "%</p>");
    }
    else { console.log(error)};
  }

  function style(feature) {
    if (feature.properties.name !== "Puerto Rico"){
      return {
          fillColor: getColor(feature.tuition.Y2015),
          weight: 2,
          opacity: 1,
          color: 'white',
          dashArray: '3',
          fillOpacity: 0.7
      };
    }
  }
  
  L.geoJson(mapData, {style: style, onEachFeature: onEachFeature}).addTo(myMap);

  // Colors by tuition magnitude
  function getColor(d) {
    return d >= .05 ? '#f50a18' :
          d >= .04 ? '#f5720a' :
          d >= .03 ? '#f39c1d' :
          d >= .02 ? '#f0cc3d' :
          d >= .01 ? '#aadb12' :
          d >= 0 ? '#8cb709' :
                    'blue';
  }

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (myMap) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, .01, .02, .03, .04, .05],
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i]) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
    }
    // Adding legend to the map   
    legend.addTo(myMap);
}
