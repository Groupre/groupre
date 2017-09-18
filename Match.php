<?php
/**
 */

function scoring_match($student, $teams, $chairs){
    /** Find a seat for student based on score.
     * Return (student, chair) tuple
     * TODO: This is the crux of team-building. Have this approved by client
    */
    for ($i = 0; $i<sizeof($teams); $i++){
        for ($j = 1; $j<sizeof($teams[0]); $j++){
            $member = $teams[$i][$j];
            if (abs($member - $student[2])==3){
                $student_chair = $teams[$j+1];
                break;
            }
        }
        }
    }

    return [$student, $student_chair];
}

/** Function takes in the stated preference, pref column, matches students into appropriate chairs. Returns array with
 *  seating chart, remaining students, remaining chairs
*/
function preference_match($preference, $pref_id, $students, $chairs){
    $seated = [];
    for ($i = 0; $i<sizeof($students); $i++){
        if ($students[$i][$pref_id] == $preference || $students[$i][$pref_id]){
            $seat = scoring_match($students[$i][0], $chairs);
            array_push($seated, $seat);

            unset($students[$seat[0]]);
            $students = array_values($students);

            unset($chairs[$seat[1]]);
            $chairs = array_values($chairs);
        }
    }
    return [$seated, $students, $chairs];
}

/** Function randomly selects student, returns chair-student relationships
*/
function random_match($students, $chairs){
    $seated = [];
    while (sizeof($students) > 0){
        $rand_student = [array_rand($students)];
        array_push($seated, scoring_match($students[$rand_student], $chairs));
        unset($students[$rand_student]);
        $remaining_ids = array_values($students);
    }
    return $seated;
}

/** Function takes in a 2D array and returns two arrays, the first has the rows that match the category
 *  and the second has the rows that do not match the category. It's select essentially
 */
function find_category($set, $category){
    $column = 0;
    for ($i=0; $i<sizeof($set[0]); $i++){
        if ($set[0][$i] == $category){
            $column = $i;
            break;
        }
    }
    $category_set = [];
    $noncategory_set = [];
    for ($i=0; $i<sizeof($set); $i++){
        if ($set[$i][$column] == $category || $set[$i][$column]) {
            $category_set[$i] = $set[$i];
        } else {
            $noncategory_set[$i] = $set[$i];
        }
    }
    return [$category_set, $noncategory_set];
}

/** Function takes in a csv file and converts yes and nos to T/F
*/

function process_csv($csv){
    for ($i=0; $i<sizeof($csv); $i++){
        for ($j=0; $j<sizeof($csv[0]); $j++){
            if ($csv[$i][$j] == "Yes"){
                $csv[$i][$j] = 1;
            }
            else if ($csv[$i][$j] == "No"){
                $csv[$i][$j] = 0;
            }
        }
    }
    return $csv;
}

$students = process_csv($students_csv);
$chairs = process_csv($chair_csv);

$split_students = find_category($students_csv, "No Priority");
$students_pref = $split_students[1];
$students_unseated = $split_students[0];

$pref = 0;
for ($i=0; $i<sizeof($chairs[0]); $i++) {
    if ($chairs[0][$i] == "Left-Handed") {
        $pref = $i;
        break;
    }
}

$seated_pref = [];
for (;$pref<sizeof($chairs[0]); $pref++){
    $seating = preference_match($chairs[0][$pref], $pref, $students_pref, $chairs);
    array_push($seated_pref, $seating[0]);
    $students_pref = $seating[1];
    $chairs = $seating[2];
}

$seated_pref = array_merge($seated_pref, random_match($students_unseated, $chairs));

