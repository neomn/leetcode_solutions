<?php

function trap($height) {
    $trappedWater = $maxLeft = $maxRight = $left = 0;
    $right = count($height) - 1;
    while($left < $right) {
        if ($height[$left] < $height[$right]) {
            $maxLeft = max($maxLeft, $height[$left]);
            $trappedWater += $maxLeft - $height[$left];
            ++$left;
        }
        else {
            $maxRight = max($maxRight, $height[$right]);
        }
    }
    return $trappedWater;
}

print_r(trap([0,1,0,2,1,0,1,3,2,1,2,1]));