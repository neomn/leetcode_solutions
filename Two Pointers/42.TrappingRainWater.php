<?php

function trap($height) {
    $trappedWater = $maxLeft = $maxRight = $left = 0;
    $right = count($height) - 1;
    while($left < $right) {

    }
    return $trappedWater;
}

print_r(trap([0,1,0,2,1,0,1,3,2,1,2,1]));