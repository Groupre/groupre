function generateGrid(rows, cols) {
    var grid = "<table>";
    grid.border = "1";
    var index = 1;
    for (row = 1; row <= rows; row++) {
        grid += "<tr>";
        for (col = 1; col <= cols; col++) {
            grid += "<td id=\"d" +index+"\"></td>";
            index++;
        }
        grid += "</tr>";
    }
    return grid;
}

var rows = parseInt(document.getElementById('Enter rows here:').value,10);
var cols = parseInt(document.getElementById('Enter columns here:').value,10);

$( "#output" ).append( generateGrid(rows, cols) );


/*

$("td").click(function() {
    cell = this;
    var index = $("td").index(this);
    var row = Math.floor((index) / 10) + 1;
    var col = (index % 10) + 1;
    $("span").text("Row = " + row + " Column = " + col + " Index = " + index);
    $(this).css('background-color', 'red');
    //$( that ).css('background-color', 'white');
    //that = this;
});

$("td").dblclick(function() {
    cell = this;
    var index = $( "td" ).index( this );
    var row = Math.floor( ( index ) / 10) + 1;
    var col = ( index % 10 ) + 1;
    $("span").text("Row = " + row + " Column = " + col + " Index = " + index);
    $(this).css('background-color', 'red');
    $(this.textContent = 'L');
    //$( that ).css('background-color', 'white');
    //that = this;
});

$("#leftHanded").click(function() {
    $(cell.textContent = 'L');
});

*/

var cell;
