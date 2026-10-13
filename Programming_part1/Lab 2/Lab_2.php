<?php
$k=2;
$w=0.0;
$x=0.0;
$y1;$y2;$y3;$y4;$y5;$y6;
define('e', '2.71828');
echo ("Please enter value for x\n");
$x=(float)readline();
$y1=pow(7.3910,-3);
$y2=$y1*$x;
$y3=pow($x,5);
$y4=pow(e,1/$k);
$y5=$y4-1;
$y6=$y3*$y5;
$w=$y2/$y6;
echo("Result is w=".$w);
?>