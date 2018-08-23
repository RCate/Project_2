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
var link2 = "4YrEnrollPctChange.json"

d3.queue()
  .defer(d3.json, link1)
  .defer(d3.json, link2)
  .await(ready);

function ready(error, mapData, csvData) {
  if(error) return console.log(error);

  
  var csvData_obj = csvData.reduce(function(acc, data){
    acc[data.State] = data
    return acc
  },{})
  mapData.features.forEach(function(feature){
    feature.enrollment = csvData_obj[feature.properties.name]
  })
  console.log(mapData);
  console.log(csvData);
  
  function onEachFeature(feature, layer) {
    console.log(feature.enrollment)
    console.log(feature.properties.name)
    if (feature.properties.name !== "Puerto Rico"){
      layer.bindPopup("<h3>" + feature.properties.name +
        "</h3><hr><p>" + feature.enrollment.Y2009 + "</p>");
    }
    else { console.log(error)};
  }

  function style(feature) {
    if (feature.properties.name !== "Puerto Rico"){
      console.log(feature)
      return {
          fillColor: getColor(feature.enrollment.Y2009),
          weight: 2,
          opacity: 1,
          color: 'white',
          dashArray: '3',
          fillOpacity: 0.7
      };
    }
  }
  
  L.geoJson(mapData, {style: style, onEachFeature: onEachFeature}).addTo(myMap);


  // Bubble colors by earthquake magnitude
  function getColor(d) {
    return d >= .05 ? '#f50a18' :
          d >= .04 ? '#f5720a' :
          d >= .03 ? '#f39c1d' :
          d >= .02 ? '#f0cc3d' :
          d >= .01 ? '#aadb12' :
          d >= 0 ? '#8cb709' :
                    'blue';
  }
}
