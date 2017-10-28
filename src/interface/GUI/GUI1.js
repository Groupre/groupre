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