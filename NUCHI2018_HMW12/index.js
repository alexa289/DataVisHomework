//Reference the variable for tbody
var $tbody = document.querySelector("tbody");

//Reference the variables on the json file
var $dateTimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector('#state');
var $countryInput = document.querySelector('#country');
var $shapeInput = document.querySelector('#shape');

//Reference the variables for the button
var $searchBtn = document.querySelector("#search");
var $resetBtn = document.querySelector("#reset");

//Add event listener to the searchBtn, add the call to the handleSearchButtonClick
$searchBtn.addEventListener('click', handleSearchButtonClick);
//Add event listener to the resetBtn
$resetBtn.addEventListener('click', resetData);

//Set filtereredData and resetData to dataSet
var resetData = dataSet;
var filteredData = dataSet;

//Create the function to render the table 
function renderTable() {
    $tbody.innerHTML = "";
    //Loop through the dataobject create new object and its inputfields
    for (var i=0; i<filteredData.lenght; i++){
        var data = filteredData[i];
        var inputfields = Object.keys(data);
        //Add a new row for tbody
        var $row = $tbody.insertRow(i);
        //Loop through each inputfield and create a new value in the cell for every field
        for (var j = 0; j<inputfields.length; j++) {
            var inputfield = inputfields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = data[inputfield];
        } 
    }
}
function handleSearchButtonClick(event) {

    // preventDefault to prevent page from refreshing
    event.preventDefault();

    var filteredDate = $dateTimeInput.value.trim();
    if (filteredDate != ""){
        filteredData = filteredData.filter(function(data){
        var dateTimeData = data.datetime;
        return dateTimeData === filteredDate;
        });
    };
    
    var filteredCountry = $countryInput.value.trim().toLowerCase();
    if (filteredCountry != "") {
        filteredData = filteredData.filter(function (data) {
            var countryData = data.country.toLowerCase();
            return countryData === filteredCountry;
        });
    };

    var filteredState = $stateInput.value.trim().toLowerCase();
    if (filteredState !="") {
        filteredData = filteredData.filter(function(data){
            var stateData = data.state.toLowerCase();
            return stateData === filteredState;
        });
    };
    
    var filteredCity = $cityInput.value.trim().toLowerCase();
    if (filteredCity != "") {
        filteredData = filteredData.filter(function (data) {
            var cityData = data.city.toLowerCase();
            return cityData === filteredCity;
        });
    }; 

    var filteredShape = $shapeInput.value.trim().toLowerCase();
    if (filteredShape) {
        filteredData = filteredData.filter(function(data){
            var shapeData = data.shape.toLowerCase();
            return shapeData === filteredShape;
        });
    };

    renderTable();
}

    function resetData() {
        filteredData = dataSet;
        $dateTimeInput.value = "";
        $cityInput.value = "";
        $stateInput.value ="";
        $countryInput.value="";
        $shapeInput.value = "";
        renderTable();
    }

    function resetForm(){
        document.getElementById("UFOForm").reset();
    }

    // Render the table for the first time on page load
    renderTable();