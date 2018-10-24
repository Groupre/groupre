$(document).ready(function(){
    var categories = {
        leftHand:'left',
        aisleLeft:'aisleleft',
        aisleRight:'aisleright',
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
    var teamName;
    
    document.getElementById('buildClass').onclick = function() {
        this.hidden = true;
        rows = parseInt(tempName.split("-")[3]);
        cols = parseInt(tempName.split("-")[4].split(".")[0]);
        teamName = document.getElementById('teamName').value;

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

                if (r == 0) {
                    cell.classList.toggle("front");
                } else if (r+1 == rows) {
                    cell.classList.toggle("back");
                }else{
                    var prop = template[index][2];
                    console.log(prop);
                    switch (prop) {
                        case "left":
                            cell.classList.toggle("leftHand");
                            break;
                        case "front" :
                            cell.classList.toggle("front");
                            break;
                        case "aisleleft" :
                            cell.classList.toggle("aisleLeft");
                            break;
                        case "aisleright" :
                            cell.classList.toggle("aisleRight");
                            break;
                        case "back" :
                            cell.classList.toggle("back");
                            break;
                        case "broken":
                            cell.classList.toggle("broken");
                            break;
    
                    }
                }
                index += 1;
                // check saved room properties
                // var prop;
                // if (r == 0) {
                //     prop = template[c][2];
                // } else if (c == 0){
                //     prop = template[r*10][2];
                // }else{
                //     prop = template[r*c][2];
                // }  
            }
            table.appendChild(row)
            prevrow = row;
        }
        document.getElementById('template').appendChild(table);
        drag();
        
        // Auto-add suggestions and selection
        var totalSeats = rows * cols;
        for (i = 2; i <= maxGroupSize; i++) {
            if (totalSeats % i == 0){
                let opt1;
                let opt2;

                if (i == 4 || i == 6){
                    opt1 = document.createElement("option");
                    opt2 = document.createElement("option");
                    opt1.value = i;
                    opt2.value = i;
                }else {
                    opt1 = document.createElement("option");
                    opt1.value = i;
                }
                if (i == 4 || i == 6){
                    opt1.innerHTML = 'Groups of ' + i + " (1 x " + i + " )";
                    opt2.innerHTML = 'Groups of ' + i + " (2 x " + i/2 + " )";
                    document.getElementById('dropdown').appendChild(opt1);   
                    document.getElementById('dropdown').appendChild(opt2);   
                }
                else{
                    opt1.innerHTML = 'Groups of ' + i;
                    document.getElementById('dropdown').appendChild(opt1);   

                }
            }
        }

           
    }

    document.getElementById("teamButton").onclick = function() {
        var table = document.getElementById("dataTable");
        var cells = table.getElementsByClassName("highlight");
        var team = document.createElement('p');

        if(cells.length < 1) {
            return;
        }

        var teamMembers = []
        for(var i=0; i<cells.length; i++) {
            var cell = cells[i];            
            for (j=0; j<teamNum; j++){
                if (cell.classList.contains("team" + j)){
                    cell.classList.toggle("team" + j);
                }
            }
            cell.classList.toggle("team" + teamNum);
            cell.innerHTML = teamNum;
            teamMembers.push(cell);
        }
        currentTeams[teamNum] = teamMembers

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

    document.getElementById("teamList").onmouseover = function() {
        var table = document.getElementById("dataTable");
        var teamList = document.getElementsByClassName("team");

        $("#teamList p").mouseover(function() {
            var team = this;
            var teamId = team.id;
            var cells = table.getElementsByClassName(teamId);
            var temp = team.innerHTML;
            team.innerHTML = cells[0].id;
        });
    }

    document.getElementById("saveTeam").onclick = function() {
        alert('save team');
        var array = [];
        array.push([roomID, teamName, rows, cols]);
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
        var chairs = JSON.stringify(array);
        setTimeout(function(){
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
            xmlhttp.open("POST", "/room-saver");
            xmlhttp.setRequestHeader("Content-Type", "application/json");
            xmlhttp.send(chairs);
        }, 1000);
        document.getElementById('notice').innerHTML = 'Team changes saved.'
        setTimeout(function(){
            document.getElementById('notice').innerHTML = ''
        }, 2000);
    }
    document.getElementById("resetTeam").onclick = function(){

    }


    // function readTextFile(filepath, callback) {
    //     var rawFile = new XMLHttpRequest();
    //     rawFile.overrideMimeType("application/json");
    //     rawFile.open("GET", filepath, true);
    //     rawFile.onreadystatechange = function() {
    //         if (rawFile.readyState === 4 && rawFile.status == "200") {
    //             callback(rawFile.responseText);
    //         }
    //     }
    //     rawFile.send(null);
    // }

    // Automatically add teams based on user selection
    document.getElementById('autoAdd').onclick = function(){
        
        var select = document.getElementById('dropdown');
        var idx = select.selectedIndex;
        var selectedOption = select.options[idx];
        var teamSize = selectedOption.value;
        var table = document.getElementById('dataTable');
        var cells = table.getElementsByTagName('td')
        var currTeam = 0;
        var teamMembers = [];
        for (var i=0; i < cells.length; i++){
            var cell = cells[i];
            cell.classList.toggle("team" + currTeam);
            cell.innerHTML = currTeam;
            teamMembers.push(cell);
            if (((i + 1) % teamSize) == 0){
                currentTeams[currTeam] = teamMembers;
                teamMembers = [];
                currTeam++;                
            }
        }
        teamNum = currTeam;        
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
});