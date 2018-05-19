// // Create the dropdown for samples
// function buildDropdown() {
//     //Plotly.d3.event.preventDefault();
//     // add samples_list to an array
//     names = [];
//     //point to names route
//     URL='http://localhost:5000/names';
//     Plotly.d3.json(URL, function (error, response){
//         if (error)
//             return console.warn(error)
        
//             names = response;

//         // loop through samples for dropdown
//         for (var i = 0; i < names.length; i++) {
//             d3.select('#selDataset')
//             .append("option")
//             .attr("value", names[i]["name"])
//             .text(names[i]);
//         }
//             optionChanged(names[0])
//     });
// }

// buildDropdown()


//-------------
function buildDropdown() {
    var selDataset = document.getElementById("selDataset");

    Plotly.d3.json('/names', function (error, data) {
        if (error) return console.warn(error)
        for (i = 0; i < data.length; i++) {
            
            var option = document.createElement("option");
            option.text = data[i]
            option.value = data[i]
            
            selDataset.appendChild(option);
        }
        //getData(data[0], buildDropdown);
    }
    )
}

buildDropdown()


// function getSampleNames() {
//     var selector = document.getElementById('selDataset');
//     var url = "/names";
//     Plotly.d3.json(url, function (error, response) {
//         if (error) return console.warn(error);
//         var data = response;
//         data.map(function (sample) {
//             var option = document.createElement('option')
//             option.text = sample
//             option.value = sample
//             selector.appendChild(option)
//         });
//     });
// };

// getSampleNames();

// function optionChanged(sample) {
//     updatePie(sample);
//     updateBubble(sample);
//     updateMetadata(sample);
// };



