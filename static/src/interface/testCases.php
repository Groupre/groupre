<?php

$zipname = 'testCases.zip';
$zip = new ZipArchive;
$zip->open($zipname, ZipArchive::CREATE);
if ($handle = opendir('.')) {
    while (false !== ($entry = readdir($handle))) {
        if ($entry != "." && $entry != ".." && !strstr($entry,'.php')) {
            $zip->addFile($entry);
        }
    }
    closedir($handle);
}

$zip->close();

header('Content-Type: application/zip');
header("Content-Disposition: attachment; filename='adcs.zip'");
header('Content-Length: ' . filesize($zipname));
header("Location: adcs.zip");