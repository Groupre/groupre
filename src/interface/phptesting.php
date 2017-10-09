<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

//$cmd = "python pythontesting.py";
//$output = shell_exec($cmd);
//echo '<pre>';
//echo ($output);
//echo '</pre>';

$cmd = "python --version";
$output = shell_exec($cmd);
print $output;
//
//header('Content-Type: application/csv');
//header('Content-Disposition: attachment; filename="err.csv"');
//readfile("err.csv");

