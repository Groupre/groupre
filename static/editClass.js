$(document).ready(function () {
    var categories = {
        leftHand: 'la',
        aisleLeft: 'al',
        aisleRight: 'ar',
        front: 'f',
        back: 'b',
        broken: 'br',
        frontish: 'fi',
        backish: 'bi'
    }
    var rows;
    var cols;
    var teamNum = 0;
    var currentTeams = {};
    var roomID;

    document.getElementById('buildClass-e').onclick = function () {
        this.hidden = true;
        rows = parseInt(tempName.split("-")[3]);
        cols = parseInt(tempName.split("-")[4].split(".")[0]);

        roomID = tempName.split("-")[1];
        var table = document.createElement('table');
        table.id = 'dataTable';
        table.border = "1";
        var prevrow;
        var index = 0;
        for (var r = 0; r < (rows); r++) {
            var row = document.createElement('tr');
            for (var c = 0; c < (cols); c++) {
                var cell = document.createElement('td');
                //need to put int to string in here to change to seat letter
                cell.id = r + ',' + c;
                cell.innerHTML = cell.id;
                // cell.innerHTML = ''
                row.appendChild(cell);

                // if (r == 0) {
                //     cell.classList.toggle("front");
                // } else if (r+1 == rows) {
                //     cell.classList.toggle("back");
                // }else{
                var attrb = template[index].slice(2, template[index].length);
                for (let x = 0; x < attrb.length; x++) {
                    let prop = attrb[x];
                    switch (prop) {
                        case "left":
                            cell.classList.toggle("leftHand");
                            break;
                        case "front":
                            cell.classList.toggle("front");
                            break;
                        case "aisleleft":
                            cell.classList.toggle("aisleLeft");
                            break;
                        case "aisleright":
                            cell.classList.toggle("aisleRight");
                            break;
                        case "back":
                            cell.classList.toggle("back");
                            break;
                        case "broken":
                            cell.classList.toggle("broken");
                            break;

                        // }
                    }

                }
                index += 1;

            }
            table.appendChild(row)
            prevrow = row;
        }
        document.getElementById('template-e').appendChild(table);
        drag();


    }
    document.getElementById("leftHandedButton-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");
        console.log("c = 1 printed");
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("leftHand");
        }

        cells = table.getElementsByTagName("td");
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }

    }

    document.getElementById("aisleButton-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");
        var hcells = table.getElementsByClassName("highlight");
        var col1 = 0;
        var col2 = 0;

        var hcell = hcells[0];
        var colStr = hcell.getAttribute("id");
        colStr = colStr[colStr.length - 1];
        // get the aisle index
        var aIndex = parseInt(colStr);
        console.log(cols, aIndex);
        if (aIndex != cols - 1) {
            for (var x = 0; x < cells.length; x++) {
                // if (x != 0 && x % cols == 0){
                //     x += cols;
                // }
                let cell = cells[x + aIndex];
                let cell1 = cells[x + aIndex + 1];
                cell.classList.toggle("aisleLeft");
                cell1.classList.toggle("aisleRight");
                x += cols - 1;

            }
        }


        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }


    document.getElementById("frontRowButton-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("front");
        }

        cells = table.getElementsByTagName("td");
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("backRowButton-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("back");
        }

        cells = table.getElementsByTagName("td");
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }
    document.getElementById("backishButton-e").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("backish");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }
    document.getElementById("frontishButton-e").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("frontish");
        }

        cells = table.getElementsByTagName("td");
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("brokenButton-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");

        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.toggle("broken");
        }

        cells = table.getElementsByTagName("td");
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            cell.classList.remove("highlight");
        }
    }

    document.getElementById("reset-e").onclick = function () {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");

        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            for (var key in categories) {
                var cat = categories[key];
                if (cell.classList.contains(key)) {
                    cell.classList.toggle(key);
                }
            }
        }
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            for (var key in currentTeams) {
                if (cell.classList.contains('team' + key)) {
                    cell.classList.toggle('team' + key);
                    cell.innerHTML = '';
                }
            }
        }
    }
    function drag() {
        var isMouseDown = false,
            isHighlighted;
        var startCell, endCell;
        $("#dataTable td")
            .mousedown(function () {
                isMouseDown = true;
                startCell = this;
                $(this).toggleClass("highlight");
                isHighlighted = $(this).hasClass("highlight");
                return false;
            })
            .mouseover(function () {
                if (isMouseDown) {
                    endCell = this;
                    var startX = startCell.id.split(',')[0]
                    var startY = startCell.id.split(',')[1]
                    var endX = endCell.id.split(',')[0]
                    var endY = endCell.id.split(',')[1]
                    if (endX < startX) {
                        var tmp = startX;
                        startX = endX;
                        endX = tmp;
                    }
                    if (endY < startY) {
                        var tmp = startY;
                        startY = endY;
                        endY = tmp;
                    }
                    for (i = startX; i <= endX; i++) {
                        for (j = startY; j <= endY; j++) {
                            var cellID = i + ',' + j;
                            var highlightedCell = document.getElementById(cellID);
                            $(highlightedCell).toggleClass("highlight", isHighlighted);
                        }
                    }
                }
            });

        $(document)
            .mouseup(function () {
                isMouseDown = false;
            });
    }


    document.getElementById('saveChanges-e').onclick = function () {
        var array = [];
        array.push([roomID, 'RowCol', rows, cols]);
        array.push(['CID', 'TeamID', 'Attributes']);

        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");

        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            var row = [];
            var cid = cell.id.split(',');
            row.push(cid[0] + cid[1]);

            for (var j = 0; j < teamNum; j++) {
                if (cell.classList.contains("team" + j)) {
                    row.push(j);
                    break;
                }
            }
            if (row.length == 1) {
                row.push(' ')
            }

            for (var key in categories) {
                var cat = categories[key];
                if (cell.classList.contains(key)) {
                    row.push(cat);
                }
            }
            array.push(row)
        }
        var classroom = JSON.stringify(array);
        setTimeout(function () {
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
            xmlhttp.open("POST", "/class-saver");
            xmlhttp.setRequestHeader("Content-Type", "application/json");
            xmlhttp.send(classroom);
        }, 1000);
        document.getElementById('message').innerHTML = 'Class template saved.'
        setTimeout(function () {
            document.getElementById('message').innerHTML = ''
        }, 2000);
    }


});