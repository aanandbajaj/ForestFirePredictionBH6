$(document.body).on('click', 'td', changeColor);

function generateGrid(rows, cols) {
  var grid = "<table>";
  for (row = 1; row <= rows; row++) {
    grid += "<tr>";
    for (col = 1; col <= cols; col++) {
      var cell = "<td> </td>";
      grid += cell;
    }
    grid += "</tr>";
  }
  $("#tableContainer").empty();
  $("#tableContainer").append(grid);
  return grid;
}

function changeColor() {
  const $this = $(this);
  if ($this.hasClass("clicked")) {
    $this.removeClass("clicked")
  } else {
    $this.addClass("clicked");
  }
}
