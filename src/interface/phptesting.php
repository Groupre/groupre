<?php
$cmd = "python pythontesting.py";
$output = shell_exec($cmd);
print($output);

header('Content-Type: application/csv');
header('Content-Disposition: attachment; filename="test.txt"');
readfile("test.txt");