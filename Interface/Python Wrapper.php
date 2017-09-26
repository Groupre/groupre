<?php

$command = escapeshellcmd('groupre.py');
$output = shell_exec($command);
echo $output;
echo 'Thank you for iusing Groupre! <br />';

?>