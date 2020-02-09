$.getJSON("map.json", function(data) {
    function generateGrid( rows, cols ) {
        for(var location in data)
        var color = false;
        var grid = "<table>";
        for ( row = 1; row <= rows; row++ ) {
            grid += "<tr>";
            for ( col = 1; col <= cols; col++ ) {
                if (color)
                    grid += "<td style='background-color: red'>yay</td>";
                else
                    grid += "<td style='background-color: blue'>yay</td>";
                color = !color;
            }
            grid += "</tr>";
        }
        return grid;
    }
    $( "#tableContainer" ).append(generateGrid(Math.sqrt(data.length), Math.sqrt(data.length)));
});