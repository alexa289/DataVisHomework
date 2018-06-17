// Store the earthquake api endpoint
var earthqURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Store the tectonic api endpoint
var tectonicURL = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

// GET request to the earthquaque query 
d3.json(earthqURL, function (data) {
    // Read the data.features object into the createFeatures function
    createFeatures(data.features);
});

function createFeatures(earthqData) {

    // Define a function to run "onEach" feature in the features array
    var earthquakes = L.geoJSON(earthqData, {
        onEachFeature: function (feature, layer) {
            layer.bindPopup("<h3>Magnitude: " + feature.properties.mag + "</h3><h3>Location: " + feature.properties.place +
                "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
        },

        pointToLayer: function (feature, latlng) {
            return new L.circle(latlng,
                {
                    radius: getRadius(feature.properties.mag),
                    fillColor: chooseColor(feature.properties.mag),
                    weight: .8,
                    color: "#000",
                    fillOpacity: .7,
                    stroke: true,
                    
                })
        }
    });


    // Create map layer for  earthquakes within the createMap function
    createMap(earthquakes);
}


function createMap(earthquakes) {

    // Define layers to be used for the map
    var light = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1IjoiYWxleGEyODkiLCJhIjoiY2poeTh6eWZpMGsxZDN3czZhZ3lkcnF5ZyJ9.IQ0x09Uvn8bDdDvUTNfhOw");

    var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1IjoiYWxleGEyODkiLCJhIjoiY2poeTh6eWZpMGsxZDN3czZhZ3lkcnF5ZyJ9.IQ0x09Uvn8bDdDvUTNfhOw");
    
    var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1IjoiYWxleGEyODkiLCJhIjoiY2poeTh6eWZpMGsxZDN3czZhZ3lkcnF5ZyJ9.IQ0x09Uvn8bDdDvUTNfhOw");

    // Create baseMaps object to hold layers

    var baseMaps = {
        "Light Layer": light,
        "Dark Layer": darkmap,
        "Satellite Layer": satellite 
    };

    // Creat a layer for the tectonic plates data
    var tectonic = new L.LayerGroup();

    // Create overlaylayer
    var overlayMaps = {
        "Tectonic P": tectonic,
        "Earthquakes": earthquakes,
    };

    // Create myMap, giving it the earthquake and tectonic layers to show on the map
    var myMap = L.map("map", {
        center: [
            37.09, -95.71],
        zoom: 3.25,
        layers: [light, earthquakes, tectonic]
    });

    // Draw tectonic lines data
    d3.json(tectonicURL, function (tectonicData) {
        // Add the Geojson tectonic plates  data with the style
        // layer.
        L.geoJson(tectonicData, {
            color: "steelblue",
            weight: 3,
            fillOpacity: 0.6
        })
            .addTo(tectonic);
    });


    
    // Add the control layer to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    //Draw the legends
    var legend = L.control({ position: 'bottomright' });

    legend.onAdd = function (myMap) {
        var div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 1, 2, 3, 4, 5],
            labels = [];

        //Loop through intervals and generate label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + chooseColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 2] ? '&ndash;' + grades[i + 3] + '<br>' : '+');
        }
        return div;
    };

    legend.addTo(myMap);
}



//Increase the maginutde of the earthquake by 30000 for the radius of the circle to actually look in the map. 
function getRadius(value) {
    return value * 30000
}

//Define a function to create the color range based on the diameter for the circle diameter. Used Orange color code in https://www.rapidtables.com/web/color/orange-color.html
function chooseColor(d) {
    return d > 5 ? "#FF4500" : //orangered
        d > 4 ? "#FF6347" :  //tomato
        d > 3 ? "#FF7F50l" : //coral
        d > 2 ? "#FF8C00" : //darkorange 
        d > 1 ? "#FFA500" : //orange
        "#FFD700"; //gold
}
