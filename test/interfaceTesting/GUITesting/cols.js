function highlight_col() {
    var table = document.getElementById('display-table');
    var cells = table.getElementsByTagName('td');

    for (var i = 0; i < cells.length; i++) {
        var cell = cells[i];
        cell.onclick = function () {
            var colId = this.parentNode.colIndex;

            var colsNotSelected = table.getElementsByTagName('tr');
            for (var col = 0; col < colsNotSelected.length; col++) {
                colsNotSelected[col].style.backgroundColor = "";
                colsNotSelected[col].classList.remove('selected');
            }
            var colSelected = table.getElementsByTagName('tr')[colId];
            colSelected.style.backgroundColor = "yellow";
            colSelected.className += " selected";

            msg = 'The column ID at the selected point is: ' + colSelected.cells[0].innerHTML;
            msg += '\nThe seat ID at the selected point is: ' + this.innerHTML;
            alert(msg);
        }
    }

}

window.onload = highlight_col;