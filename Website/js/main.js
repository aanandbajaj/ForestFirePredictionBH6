$(document.body).on('click', 'td');

d3.csv("../mapfile.csv").then(function(data) {
  var all_data,
    xCoor,
    yCoor,
    type,
    fire,
    time;
  rows = 30;
  cols = 30;
  indexLocations = [];

  indexLocations = getStartingIndices();

  for (var i = 0; i < 5; i++) {
    init(indexLocations[i]);
  }

  function init(index) {
    var xCounter, yCounter;
    xCounter = 1;
    yCounter = 1;

    //currentIndex is for the data
    //but need to know which row am on
    var currentIndex = index - 2;
    var color;

    var tableExist = document.getElementById("mapTable");
    if(tableExist){
      $("#mapTable").remove();
    }

    var body = document.body,
      tbl = document.createElement('table');
    tbl.style.width = '1000px';
    tbl.style.border = '1px solid black';
    tbl.setAttribute("id", "mapTable", 0);

    setFields(currentIndex);
    //currentIndex is which row we are on on the csv

    for (var i = 0; i < rows; i++) {
      var tr = tbl.insertRow();
      for (var j = 0; j < cols; j++) {
        var td = tr.insertCell();
        color = getColors(type,fire);
        //td.appendChild(document.createTextNode('Cell'));
        td.style.background = color;
        xCounter++;
        currentIndex++;
        setFields(currentIndex);
      }
      yCounter++;
    }
    body.appendChild(tbl);
  }

  function setFields(index) {
    xCoor = data[index].X;
    yCoor = data[index].Y;
    type = data[index].Type;
    fire = data[index].Fire;
    time = data[index].Time;
  }

  function getColors(tileType, isFire) {
    //field
    //forest
    //river
    if (isFire.includes("True")){
      return "#ff0000";
    }


    if (tileType.includes("TerrainType.Field")) {
      return "#14d752";
    } else if (tileType.includes("TerrainType.Forest")) {
      return "#0c8332";
    } else if (tileType.includes("TerrainType.River")) {
      return "#14a6d7";
    }

  }

  function getStartingIndices() {
    var startingIndices = new Array();

    for (var i = 0; i < data.length; i++) {
      if (data[i].X == 1 && data[i].Y == 1) {
        startingIndices.push(i + 2);
      } else {

      }
    }
    return startingIndices;

  }

});
