function jsFunction(value) {
    $("#dataTable td").removeClass("highlight");
    switch(value) {
        case 'cols':
            //alert('cols');
            $("#dataTable tr td").click(function() {
                //Reset
                $("#dataTable td").removeClass("highlight");
                //Add highlight class to new column
                var index = $(this).index();
                $("#dataTable tr").each(function(i, tr) {
                    $(tr).find('td').eq(index).addClass("highlight");
                });
              });
            break;

        case 'rows':
            //alert('rows');
            $("#dataTable tr").click(function() {
                //Reset
                $("#dataTable td").removeClass("highlight");
                //Add highlight class to new column
                var row = $(this).rowIndex;
                $(this).find('td').each (function(i, td) {
                    $(td).addClass("highlight");
                  });       
              });
            break;
        
        case 'front':
            $("#dataTable tr").click(function() {
                //Reset
                //$("#dataTable td").toggleClass("front");
                //Add highlight class to new column
                var row = this.rowIndex;
                $(this).find('td').each (function(i, td) {
                    /*if($(this).hasClass("back")) {
                        alert($(this).hasClass("back"));
                        $(this).toggleClass("back", false);
                    }*/
                    $(this).toggleClass("front");
                });       
            });
            break;
            
        case 'back':
            $("#dataTable tr").click(function() {
                //Reset
                //$("#dataTable td").toggleClass("front");
                //Add highlight class to new column
                var row = this.rowIndex;
                $(this).find('td').each (function(i, td) {
                    $(this).toggleClass("back");
                });       
            });
            break;

        case 'drag':
            var isMouseDown = false,
            isHighlighted;
            $("#dataTable td")
            .mousedown(function () {
                isMouseDown = true;
                $(this).toggleClass("highlight");
                isHighlighted = $(this).hasClass("highlight");
                return false;
            })
            .mouseover(function () {
                if (isMouseDown) {
                $(this).toggleClass("highlight", isHighlighted);
                }
            });
        
            $(document)
            .mouseup(function () {
                isMouseDown = false;
            });
            break;
    }
}

document.getElementById('build').onclick = function() {
    var rows = parseInt(document.getElementById('Enter rows here:').value,10);
    var cols = parseInt(document.getElementById('Enter columns here:').value,10);
    var table = document.createElement('table');
    table.id = 'dataTable';
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

/*function colSelect() {
    $("#dataTable tr td").click(function() {
        //Reset
        $("#dataTable td").removeClass("highlight");
        //Add highlight class to new column
        var index = $(this).index();
        $("#dataTable tr").each(function(i, tr) {
            $(tr).find('td').eq(index).addClass("highlight");
        });
      });
}*/

/*function rowSelect() {
    alert("test");
    $("#dataTable tr td").click(function() {
        //Reset
        $("#dataTable td").removeClass("highlight");
        //Add highlight class to new column
        var row = $(this).rowIndex();
        $("#dataTable tr").each(function(i, tr) {
            $(tr).find('td').eq(index).addClass("highlight");
        });
      });
}*/

/*function rowSelect() {
    $("#dataTable tr").click(function() {
        //Reset
        $("#dataTable td").removeClass("highlight");
        //Add highlight class to new column
        var row = $(this).rowIndex();
        $("#dataTable tr").each(function(i, tr) {
            $(tr).eq(row).addClass("highlight");
        });
      });
}*/

/*function rowSelect() {
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
}*/
