$(document).ready(function(){
    var categories = {
        leftHand:'left',
        aisleLeft:'aisle',
        aisleRight:'aisle',
        front:'front',
        back:'back',
        broken:'broken'
    }
    var rows;
    var cols;
    var maxGroupSize = 6;
    var teamNum = 0;    
    var currentTeams = {};
    var roomID;

    
    document.getElementById('build').onclick = function() {
        this.hidden = true;
        rows = parseInt(document.getElementById('Enter rows here:').value,10);
        cols = parseInt(document.getElementById('Enter columns here:').value,10);
        roomID = document.getElementById('roomID').value;
	console.log(roomID);
        var table = document.createElement('table');
        table.id = 'dataTable';
        table.border = "1";
        var prevrow;
        for (var r = 0; r < (rows); r++) {
            var row = document.createElement('tr');
            for (var c = 0; c < (cols); c++) {
                var cell = document.createElement('td');
                //need to put int to string in here to change to seat letter
                cell.id = r + ',' + c;
                cell.innerHTML = cell.id;
                // cell.innerHTML = ''
                row.appendChild(cell);
                if (c== 0){
                    cell.classList.toggle("leftHand");
                } else if (r == 0) {
                    cell.classList.toggle("front");
                } else if (r+1 == rows) {
                    cell.classList.toggle("back");
                }
            }

            table.appendChild(row)
            prevrow = row;
        }
        document.getElementById('output').appendChild(table);
        drag();
    }

    //Automatically add teams based on user selection
    // document.getElementById('autoAdd').onclick = function(){
    //     // Auto-add suggestions and selection
    //     var totalSeats = rows * cols;
    //     for (i = 2; i <= maxGroupSize; i++) {
    //         if (totalSeats % i == 0){
    //             var opt = document.createElement("option");
    //             opt.value = i;
    //             opt.innerHTML = 'Groups of ' + i;
	// 	console.log(i);
    //             document.getElementById('dropdown').appendChild(opt);   
    //         }
    //     }

    //     var select = document.getElementById('dropdown');
    //     var idx = select.selectedIndex;
    //     var selectedOption = select.options[idx];
    //     var teamSize = selectedOption.value;
    //     var table = document.getElementById('dataTable');
    //     var cells = table.getElementsByTagName('td')
    //     var currTeam = 0;
    //     var teamMembers = [];
    //     for (var i=0; i < cells.length; i++){
    //         var cell = cells[i];
    //         cell.classList.toggle("team" + currTeam);
    //         cell.innerHTML = currTeam;
    //         teamMembers.push(cell);
    //         if (((i + 1) % teamSize) == 0){
    //             currentTeams[currTeam] = teamMembers;
    //             teamMembers = [];
    //             currTeam++;                
    //         }
    //     }
    //     teamNum = currTeam;        
    // }

    function addToTeam(cell, team){
        //TODO use this function for whenever we add to teams
    }

    function matchRuleShort(str, rule) {
        return new RegExp("^" + rule.split("*").join(".*") + "$").test(str);
      }

    document.getElementById("leftHandedButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");
        console.log("c = 1 printed");
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

                cells[i+1].classList.toggle("leftHand");

            } else if(col1 == 0 && col2 == 0) {
                col1 = col;
                if(col > nextCol) {
                    col2 = col;
                    col1 = nextCol;
                    cell.classList.toggle("aisleRight");

                } else {
                    cell.classList.toggle("aisleLeft");
                    cells[i+1].classList.toggle("leftHand");

                }
            } else {
                if(col == col1) {
                    cell.classList.toggle("aisleLeft");
                    cells[i+1].classList.toggle("leftHand");

                } else if(col == col2) {
                    cell.classList.toggle("aisleRight");

                }
            }
        }

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
                if (cell.classList.contains(key)){
                    cell.classList.toggle(key);
                }
            }
        }
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            for (var key in currentTeams){
                if (cell.classList.contains('team' + key)){
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
            var endX =  endCell.id.split(',')[0]
            var endY = endCell.id.split(',')[1]
            if (endX < startX){
                var tmp = startX;
                startX = endX;
                endX = tmp;
            }
            if (endY < startY){
                var tmp = startY;
                startY = endY;
                endY = tmp;  
            }
            for (i = startX; i <= endX; i++){
                for (j = startY; j <= endY; j++){
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
    

    document.getElementById('saveChanges').onclick = function(){
        var array = [];
        array.push([roomID, 'default', rows, cols]);
        array.push(['CID', 'TeamID', 'Attributes']);

        var table = document.getElementById("dataTable");
        var cells = table.getElementsByTagName("td");
        
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];
            var row = [];
            var cid = cell.id.split(',');
            row.push(cid[0] + cid[1]);

            for (var j=0; j<teamNum; j++) {
                if (cell.classList.contains("team"+j)){
                    row.push(j);
                    break;
                }
            }
            if (row.length == 1){
                row.push(' ')
            }

            for(var key in categories) {
                var cat = categories[key];
                if (cell.classList.contains(key)){
                    row.push(cat);
                }
            }
            array.push(row)
        }
        var classroom = JSON.stringify(array);
        setTimeout(function(){
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
            xmlhttp.open("POST", "/class-saver");
            xmlhttp.setRequestHeader("Content-Type", "application/json");
            xmlhttp.send(classroom);
        }, 1000);
        document.getElementById('message').innerHTML = 'Changes saved.'
        setTimeout(function(){
            document.getElementById('message').innerHTML = ''
        }, 2000);
    }

    
});
