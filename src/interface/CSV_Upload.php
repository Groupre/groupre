<?php
/**
 *
 */

$upload_dir = "src/interface/uploads/";
$upload_file = $upload_dir . basename($_FILES['userfile'] ['name']);

$uploadsuccess = 1;


/** Check to ensure that the file is a CSV
 */
if(isset($_POST["submit"])) {
    if (pathinfo($upload_file,PATHINFO_EXTENSION) != "csv"){
        echo "File is not a CSV";
        $uploadsuccess = 0;
    }
}

/** Check error codes and print relevant info.
 */

switch ($_FILES['userfile']['error']){
    case 0:
        echo "Upload OK.";
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
    echo '<pre>';

    if (move_uploaded_file($_FILES['userfile']['tmp_name'], $upload_file)){
        echo "CSV successfully uploaded.";
    } else {
        echo "Failed to upload. Printing info.\n";
    }

    echo "Info:";
    print_r($_FILES);

    print "</pre>";

    $students_csv = $_FILES['userfile'];
    //include("Match.php");
//    $file = fopen("/home/jose/Documents/rosters/students.csv", 'x+');
//    fputcsv($file, $students_csv);

    /** Allows user to download assigned_seats.csv
     */

    //header("Content-Disposition: attachment; filename=\"" . basename($assigned_seats) . "\"");

}



