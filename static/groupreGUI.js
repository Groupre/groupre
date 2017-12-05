$(document).ready(function(){
    var categories = {
        left:'l',
        aisleL:'a',
        aisleR:'a',
        front:'f',
        back:'b',
        broken:'broken'
    }
    var rows;
    var cols;
    var roomID = document.getElementById('roomName').value;
    
    document.getElementById('build').onclick = function() {
        rows = parseInt(document.getElementById('Enter rows here:').value,10);
        cols = parseInt(document.getElementById('Enter columns here:').value,10);
        var table = document.createElement('table');
        table.id = 'dataTable';
        table.border = "1";
        var prevrow;
        for (var r = 0; r < (rows); r++) {
            var row = document.createElement('tr');
            for (var c = 0; c < (cols); c++) {
                var cell = document.createElement('td');
                //need to put int to string in here to change to seat letter
                cell.id = 'Seat ' + r + ' ' + c;
                cell.innerHTML = cell.id;
                row.appendChild(cell);
            }
            if (prevrow) {
                table.insertBefore(row, prevrow);
            } else {
                table.appendChild(row);
            }
            prevrow = row;
        }
        document.getElementById('output').appendChild(table);
        drag();
    }

    document.getElementById("leftHandedButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("leftHand");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }

    }

    document.getElementById("aisleButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");
        var col1 = 0;
        var col2 = 0;

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            var colStr = cell.getAttribute("id");
            colStr = colStr[colStr.length-1];
            var col = parseInt(colStr);

            if(i<cells.length-1) {
                var nextColStr = cells[i+1].getAttribute("id");
                nextColStr = nextColStr[nextColStr.length-1];
                var nextCol = parseInt(nextColStr);
            }

            if(col == 0) {
                cell.classList.toggle("aisleLeft");
            } else if(col1 == 0 && col2 == 0) {
                col1 = col;
                if(col > nextCol) {
                    col2 = col;
                    col1 = nextCol;
                    cell.classList.toggle("aisleRight");
                } else {
                    cell.classList.toggle("aisleLeft");
                }
            } else {
                if(col == col1) {
                    cell.classList.toggle("aisleLeft");
                } else if(col == col2) {
                    cell.classList.toggle("aisleRight");
                }
            }
        }

        /*for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            var col = cell.getAttribute("id");
            alert(col[col.length-1]);
        }

        /*for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("aisle");
        }*/

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("frontRowButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("front");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("backRowButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("back");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("brokenButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("broken");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("reset").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            for(var key in categories) {
                var cat = categories[key];
                if (cell.classList.contains(cat)){
                    cell.classList.toggle(cat);
                }
            }
        }
    }
    
    var teamNum = 0;

    document.getElementById("teamButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");
        var team = document.createElement('p');

        if(cells.length < 1) {
            return;
        }

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("team" + teamNum);
        }

        team.innerHTML = "Team " + teamNum;
        team.id = "team" + teamNum;
        teamNum += 1;
        document.getElementById("teamList").appendChild(team);

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("teamList").onclick = function() {
        var table = document.getElementById("dataTable");
    }


    function drag() {
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
    }

    document.getElementById('saveChanges').onclick = function(){
        var array = [];
        //TODO add roomID form in groupreHome.html
        array.push([roomID, 'default', rows, cols]);
        array.push(['CID', 'TeamID', 'Attributes']);

        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");
        
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            var row = [];
            row.push(cell.innerHTML);

            for (var j=0; j<teamNum; j++) {
                if (cell.classList.contains('team' + j)){
                    row.push(j);
                    break;
                }
            }
            if (row.length == 1){
                row.push(' ')
            }

            for(var key in categories) {
                var cat = categories[key];
                if (cell.classList.contains(cat)){
                    row.push(cat);
                }
            }
            array.push(row)
        }
        var chairs = JSON.stringify(array);
        setTimeout(function(){
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
            xmlhttp.open("POST", "/json-handler");
            xmlhttp.setRequestHeader("Content-Type", "application/json");
            xmlhttp.send(chairs);
        }, 1000);
    }
});
