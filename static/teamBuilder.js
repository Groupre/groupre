$(document).ready(function(){
    var rows;
    var cols;
    var maxGroupSize = 6;
    var teamNum = 0;    
    var currentTeams = {};
    var roomID;
    
    var template= null;

    // Selects the room from template and builds it. 
    document.getElementById('buildRoom').onclick = function(){
        
        var select = document.getElementById('classList');
        var idx = select.selectedIndex;
        var selectedOption = select.options[idx].text;
        
        var filepath = '/uploads/classrooms/' + selectedOption;

        // this doesnt work because the server file cant be access directly 
        readTextFile(filepath, function(text){
        var data = JSON.parse(text);
        alert(data);
            });

            /** design pattern get name here sent xttp request to flask
            flask gets the string and search server for file
            load the file and return new page for built room 
            */
        
    }
    // Automatically add teams based on user selection
    document.getElementById('autoAdd').onclick = function(){
        // Auto-add suggestions and selection
        var totalSeats = rows * cols;
        for (i = 2; i <= maxGroupSize; i++) {
            if (totalSeats % i == 0){
                var opt = document.createElement("option");
                opt.value = i;
                opt.innerHTML = 'Groups of ' + i;
		console.log(i);
                document.getElementById('dropdown').appendChild(opt);   
            }
        }

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
        var chairs = JSON.stringify(array);
        setTimeout(function(){
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
            xmlhttp.open("POST", "/room-saver");
            xmlhttp.setRequestHeader("Content-Type", "application/json");
            xmlhttp.send(chairs);
        }, 1000);
        document.getElementById('message').innerHTML = 'Changes saved.'
        setTimeout(function(){
            document.getElementById('message').innerHTML = ''
        }, 2000);
    }


    function readTextFile(filepath, callback) {
        var rawFile = new XMLHttpRequest();
        rawFile.overrideMimeType("application/json");
        rawFile.open("GET", filepath, true);
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
                callback(rawFile.responseText);
            }
        }
        rawFile.send(null);
    }
    
      
    

});