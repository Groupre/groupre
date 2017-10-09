<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="test.css" type="text/css">
    <title>groupre</title>
</head>
<body>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

//$cmd = "python pythontesting.py";
//$output = shell_exec($cmd);
//echo '<pre>';
//echo ($output);
//echo '</pre>';

$cmd = "python --version &> err.txt";
$output = shell_exec($cmd);
echo '<pre>';
echo ($output);
echo '</pre>';

header('Content-Type: application/csv');
header('Content-Disposition: attachment; filename="err.txt"');
readfile("err.txt");
?>
</body>
</html>
