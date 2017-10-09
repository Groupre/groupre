<?php
/**
 *
 */

$upload_dir = __DIR__.'/uploads/';
$upload_file = $upload_dir . basename($_FILES['userfile'] ['name']);
echo "<br>";
echo $upload_file;
echo "<br>";

$uploadsuccess = 1;


/** Check to ensure that the file is a CSV
 */
//if(isset($_POST["submit"])) {
//    if (pathinfo($upload_file,PATHINFO_EXTENSION) != "text/csv"){
//        echo "File is not a CSV";
//        $uploadsuccess = 0;
//    }
//}

echo "<br>";
echo "Upload success: ".$uploadsuccess;
echo "<br>";
/** Check error codes and print relevant info.
 */

switch ($_FILES['userfile']['error']){
    case 0:
        echo "No error in file.";
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
    echo "Failed to upload.";
} else {
    $students_csv = '';
    copy($upload_file, $students_csv);

    echo '<pre>';

    if (move_uploaded_file($_FILES['userfile']['tmp_name'], $upload_file)){
        echo "CSV successfully uploaded.";
    } else {
        echo "Failed to upload. Printing info:\n";
    }

    print_r($_FILES);

    print "</pre>";


    $cmd = "python groupre.py chairsTest.csv " . $students_csv;
    $output = shell_exec($cmd);
    print $output;

    header('Content-Type: application/csv');
    header('Content-Disposition: attachment; filename="output.csv"');
    readfile("output.csv");
}



