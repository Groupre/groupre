$(document).ready(function(){
    document.getElementById('build').onclick = function() {
        var rows = parseInt(document.getElementById('rows').value,10);
        var cols = parseInt(document.getElementById('cols').value,10);
        function tableCreate(rows) {
            var board = document.getElementById('board'),
            tbl = document.createElement('table');
            tbl.style.width = '100px';

            for (var i = 0; i < rows; i++) {
                var tr = tbl.insertRow();
                for (var j = 0; j < cols; j++) {
                    var td = tr.insertCell();
                    td.appendChild(document.createTextNode('Cell'));
                    td.style.border = '1px solid black'
                }
            }
            board.appendChild(tbl);
        }
        tableCreate(rows);
    };
}
