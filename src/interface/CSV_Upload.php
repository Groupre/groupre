<?php
/**
 *
 */

function endsWith($haystack, $needle)
{
    $length = strlen($needle);

    return $length === 0 ||
        (substr($haystack, -$length) === $needle);
}

$upload_dir = __DIR__.'/uploads/';
$upload_file = $upload_dir . basename($_FILES['userfile'] ['name']);
$students_csv = $upload_file;
//echo "<br>";
//echo $upload_file;
//echo "<br>";

$uploadsuccess = 1;


/** Check to ensure that the file is a CSV
 */
//if(isset($_POST["submit"])) {
//    if (pathinfo($upload_file,PATHINFO_EXTENSION) != "text/csv"){
//        echo "File is not a CSV";
//        $uploadsuccess = 0;
//    }
//}

//echo "<br>";
//echo "Upload success: ".$uploadsuccess;
//echo "<br>";
/** Check error codes and print relevant info.
 */

switch ($_FILES['userfile']['error']){
    case 0:
//        echo "No error in file.";
        $uploadsuccess = 1;
        break;
    case 1:
        echo "File exceeds upload_max_filesize in php.ini.";
        break;
    case 2:
        echo "File exceeds MAX_FILE_SIZE set in HTML tag.";
        break;
    case 3:
        echo "File only partially uploaded.";
        break;
    case 4:
        echo "No file uploaded.";
        break;
    case 6:
        echo "Missing temp folder.";
        break;
    case 7:
        echo "Failed to write to disk.";
        break;
    case 8:
        echo "PHP extension error. Check PHP extensions.";
        break;
    default:
        echo "Unknown error.";
        break;
}

/**Attempt upload if no errors are detected.
 **/
if ($uploadsuccess == 0){
//    echo "Failed to upload.";
} else {
//    echo '<pre>';

    if (move_uploaded_file($_FILES['userfile']['tmp_name'], $upload_file)){
//        echo "CSV successfully uploaded.";
    } else {
//        echo "Failed to upload. Printing info:\n";
    }

//    print_r($_FILES);

//    print "</pre>";

    #TODO hotfix here; get rid of later
    $test_dir = __DIR__.'/../../test/testFiles/';
    $groupre = 'python ' . __DIR__'/../python/groupre27.py'
    switch ($students_csv) {
        case endsWith($students_csv, 't.csv'):
            $chairs_csv = $test_dir.'chairs/chairsTest.csv';
            $cmd = $groupre.' '. $chairs_csv.' '.$students_csv;
            $output = shell_exec($cmd);
            break;
        case endsWith($students_csv, '2.csv'):
            $chairs_csv = $test_dir.'chairs/chairsTest2.csv';
            $cmd = $groupre.' '. $chairs_csv .' '.$students_csv;
            $output = shell_exec($cmd);
            break;
        case endsWith($students_csv, '3.csv'):
            $chairs_csv = $test_dir.'chairs/chairsTest3.csv';
            $cmd = $groupre.' '. $chairs_csv.' '.$students_csv;
            $output = shell_exec($cmd);
            break;
        default:
            $students_csv = $test_dir.'students/studentsTest.csv';
            $chairs_csv = $test_dir.'chairs/chairsTest.csv';
            $cmd = $groupre.' '. $chairs_csv.' '.$students_csv;
            $output = shell_exec($cmd);
            break;
    }

    header('Content-Type: application/csv');
    header('Content-Disposition: attachment; filename="output.csv"');
    readfile("output.csv");
}



