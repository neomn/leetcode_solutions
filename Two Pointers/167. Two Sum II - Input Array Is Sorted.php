<?php

function twoSum($numbers, $target) {

    $edgePointerleft = 0;
    $edgePointerRight = count($numbers)-1;
    $middlePointerLeft = floor(count($numbers)/2)-1;
    $middlePointerRight = $middlePointerLeft+1;

    echo $edgePointerleft,$edgePointerRight,$middlePointerLeft,$middlePointerRight;

}

print_r( twoSum([-19,-12,-6,-4,-3,-1,0,1,6,8,12,16,20],9) );
