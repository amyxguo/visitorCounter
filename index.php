<?php

$num = exec("python readCounter.py");
echo $num;
exec("python writeCounter.py $num");

$myFile = "timeVisited.txt";
$fh = fopen($myFile, 'a') or die("can't open file");
$time = date('l jS \of F Y h:i:s A');
fwrite($fh, $time . "\n");
fclose($fh);
?>
