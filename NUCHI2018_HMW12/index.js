//Reference the variables on the json file
var $dateTime = document.querySelector("#datetime");
var $city = document.querySelector("#city");
var $state = document.querySelector('#state');
var $country = document.querySelector('#country');
var $shape = document.querySelector('#shape');
var $durationMinutes = document.querySelector('#durationMinutes');
var $comments = document.querySelector('#comments');
//Reference the variable for tbody
var $tbody = document.querySelector('tbody')
//Reference the variables for the button
// var $searchBtn = document.querySelector('#search');
// var $resetBtn = document.querySelector('#reset');

// //Add event listener to the searchBtn, add the call to the handleSearchButtonClick
// $searchBtn.addEventListener('click', handleSearchButtonClick);
// //Add event listener to the resetBtn
// $resetBtn.addEventListener('click', resetData);

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
            var $cellValue = $row.insertCell(j);
            $value.innerText = data[field];
        } 
    }
}
function handleSearchButtonClick(event) {
    // preventDefault to prevent page from refreshing
    event.preventDefault();

    var filteredDate = $dateTime.value.trim();
    if (filteredDate != ""){
        filteredData = dataSet.filter(function(data){
        var dateTimeData = data.datetime;
        return dateTimeData === filteredDate;
        });
    };

    var filteredCity = $city.value.trim().toLowerCase();
    if (filteredCity != "") {
        filteredData = filteredData.filter(function(data){
            var cityData = data.city.toLowerCase();
            return cityData === filteredCity;
        });
    }; 

    


}