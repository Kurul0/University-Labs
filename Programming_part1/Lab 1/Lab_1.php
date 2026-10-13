<?php
$n=0;
$i=0;
$s=0;
echo ("Please enter value for N\n");
$n=(int)readline();
$s=0;
for($i=1; $i<=$n; $i+=1)
{
    if ($i % 2 == 0)
    {
        $s=$s+$i;
        echo ("Current value i=".$i."S=".$s);
        echo ("\n");
    }
}
echo ("Final result suma is S=".$s);
?>