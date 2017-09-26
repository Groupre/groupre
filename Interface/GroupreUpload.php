<?php

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["targetCSV"]["name"]);
$uploadOk = 1;
$fileType = pathinfo($target_file,PATHINFO_EXTENSION);{

}
// check if already there
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}

// Check for csv
if($fileType != "csv" ) {
    echo "Invalid file type.";
    $uploadOk = 0;
}
// upload error check
if ($uploadOk == 0) {
    echo "Whoops, we seem to have had a problem with your file. Please try again.";
    
// do upload thingy
} else {
    if (move_uploaded_file($_FILES["targetCSV"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["targetCSV"]["name"]). " has been uploaded.";
    } else {
        echo "Whoops, we seem to have had a problem with your file. Please try again.";
    }
}
?>