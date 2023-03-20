<?php

function threeSum($nums) {
    $result = [];
    sort($nums);
    $length = count($nums);
    for ($i = 0; $i < $length - 2; $i++) {
        if ($i > 0 && $nums[$i] == $nums[$i - 1])
            continue;
        $left = $i + 1;
        $right = $length - 1;
    }
}

$nums = [-5,-8,-15,54,0,5,3,-7,1,0,2,43,-1,12,-3,0,6,1,9];
print_r( threeSum($nums) );