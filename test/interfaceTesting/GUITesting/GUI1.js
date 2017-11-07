function jsFunction(value)
{
    alert(value);
}

document.getElementById('build').onclick = function() {
    var rows = parseInt(document.getElementById('Enter rows here:').value,10);
    var cols = parseInt(document.getElementById('Enter columns here:').value,10);
    var table = document.createElement('table');
    table.border = "1";
    var prevrow;
    for (var r = 0; r < (rows); r++) {
        var row = document.createElement('tr');
        for (var c = 0; c < (cols); c++) {
            var col = document.createElement('td');
            //need to put int to string in here to change to seat letter
            col.id = 'Seat ' + r + ' ' + c;
            col.innerHTML = col.id;
            row.appendChild(col);
        }
        if (prevrow) {
            table.insertBefore(row, prevrow);
        } else {
            table.appendChild(row);
        }
        prevrow = row;
    }
    document.getElementById('output').appendChild(table);
}

function drag() {
  var isMouseDown = false,
    isHighlighted;
  $("#output td")
    .mousedown(function () {
      isMouseDown = true;
      $(this).toggleClass("highlighted");
      isHighlighted = $(this).hasClass("highlighted");
      return false;
    })
    .mouseover(function () {
      if (isMouseDown) {
        $(this).toggleClass("highlighted", isHighlighted);
      }
    });

  $(document)
    .mouseup(function () {
      isMouseDown = false;
    });
}

function highlight_row() {
    var table = document.getElementById('display-table');
    var cells = table.getElementsByTagName('td');

    for (var i = 0; i < cells.length; i++) {
        var cell = cells[i];
        cell.onclick = function () {
            var rowId = this.parentNode.rowIndex;

            var rowsNotSelected = table.getElementsByTagName('tr');
            for (var row = 0; row < rowsNotSelected.length; row++) {
                rowsNotSelected[row].style.backgroundColor = "";
                rowsNotSelected[row].classList.remove('selected');
            }
            var rowSelected = table.getElementsByTagName('tr')[rowId];
            rowSelected.style.backgroundColor = "yellow";
            rowSelected.className += " selected";

            msg = 'The row ID at the selected point is: ' + rowSelected.cells[0].innerHTML;
            msg += '\nThe seat ID at the selected point is: ' + this.innerHTML;
            alert(msg);
        }
    }

}

window.onload = highlight_row;
