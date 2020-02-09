function generateGrid( rows, cols ) {
    var grid = "<table>";
    for ( row = 1; row <= rows; row++ ) {
        grid += "<tr>"; 
        for ( col = 1; col <= cols; col++ ) {      
            grid += "<td></td>";
        }
        grid += "</tr>"; 
    }
    return grid;
}

$( "#tableContainer" ).append( generateGrid( 5, 5) );

$( "td" ).click(function() {
    var index = $( "td" ).index( this );
    var row = Math.floor( ( index ) / 5) + 1;
    var col = ( index % 5 ) + 1;
    $( "span" ).text( "That was row " + row + " and col " + col );
    $( this ).css( 'background-color', 'red' );
});