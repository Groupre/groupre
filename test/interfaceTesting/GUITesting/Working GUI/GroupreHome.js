var seatMarksRemaining;
var leftToDiscover;
var seatArrayThingy = new Array();
var runProgram = false;

function init() {
    $(document).bind("contextmenu", function (e) {

        return false;
    });
    $('#Chairs').html('');
    columns = $("[name='columns']").val();
    rows = $("[name='rows']").val();

    availSeats = $("[name='availSeats']").val();

    seatMarksRemaining = availSeats + columns*rows;
    leftToDiscover = columns * rows - availSeats;

    $('#Classroom').width(columns * 20);
    $('#Classroom').height(rows * 20);
    $('#seatsLeft').html("0" + seatMarksRemaining);
    
    for (var i = 0; i < rows; i++) {

        seatArrayThingy[i] = new Array();
        
        for (var j = 0; j < columns; j++) {

            seatArrayThingy[i][j] = 0;

            $("#Chairs").append("<input type='button' class='square' id="+i+"_"+j+" value='' onclick='clickChair("+i+","+j+")' oncontextmenu='seatMarkFunc("+i+","+j+")'/>"); //event.onshiftKey??? event.shiftKey??? onshiftKey??? none of it is working!!!

        }

        $("#Chairs").append('<br>');

    }

    var i = 0;
    while (i < availSeats) {

        var x = Math.floor(Math.random() * rows);
        var y = Math.floor(Math.random() * columns);

        while (seatArrayThingy[x][y] === 0) {

            seatArrayThingy[x][y] = 1;
            i++;
            break;
        }
    }
    runProgram = true;

}

function clickChair(i, j) {

    while (seatArrayThingy[i][j] > 1) {

        seatMarkFunc(i, j);

    } while (seatArrayThingy[i][j] == 1) {

        $("#"+i+"_"+j).addClass("active");
        runProgram = false;
        showChairs();
        break;

    } if (seatArrayThingy[i][j] < 1) {

        $("#"+i+"_"+j).addClass("active");
        $("#"+i+"_"+j).attr('onclick', '');
        leftToDiscover--;

        var number = countChairs(i, j);
        if (number !== 0) {
            $("#"+i+"_"+j).prop('value', number);

        }else

            for (var x = Math.max(0, i-1); x <= Math.min(rows-1, i+1); x++)

                for (var y = Math.max(0, j-1); y <= Math.min(columns-1, j+1); y++)

                    if (seatArrayThingy[x][y] < 2 && !$("#"+x+"_"+y).hasClass('active')) clickChair(x, y);
                        
                        win();

    }
}

function countChairs(i, j) {

    var chairCount = 0;
    for (var x = Math.max(0, i-1); x <= Math.min(rows-1, i+1); x++)

        for (var y = Math.max(0, j-1); y <= Math.min(columns-1, j+1); y++)

    if (seatArrayThingy[x][y] == 1 || seatArrayThingy[x][y] == 3) chairCount++;
    return chairCount;
  
}

function seatMarkFunc(i, j) {

    if (!$("#"+i+"_"+j).hasClass('active')) {

        if (seatArrayThingy[i][j] < 2) {

            if (seatMarksRemaining > 0) {

                seatArrayThingy[i][j] += 2;
                $("#"+i+"_"+j).prop('value', "🐟");
                $("#"+i+"_"+j).css("color", "#FF0000");
                seatMarksRemaining--;
            }

        } else {

            seatArrayThingy[i][j] -= 2;
            $("#"+i+"_"+j).prop('value', "");
            $("#"+i+"_"+j).css("color", "");
            seatMarksRemaining++;

        }
    }

    $('#seatsLeft').html("0" + seatMarksRemaining);
}

function showChairs() {

    for (var i = 0; i < rows; i++)

        for (var j = 0; j < columns; j++) {

        while (seatArrayThingy[i][j] == 1) {
            $("#"+i+"_"+j).prop('value', "💣");
            $("#"+i+"_"+j).css("font-size", "10px");
            $("#"+i+"_"+j).css("background-color", "#FF0000");
            break;
        }

        $("#"+i+"_"+j).attr('onclick', 'init()');

    }

}
