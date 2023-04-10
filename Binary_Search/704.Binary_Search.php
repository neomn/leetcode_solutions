<?php

function search($nums, $target){
    $left = 0;
    $right = count($nums) - 1;
    while ($left <= $right) {
        $mid = $left + floor(($right - $left) / 2);
        if ($nums[$mid] == $target)
            return $mid;
        elseif ($nums[$mid] < $target)
            $left = $mid + 1;
        else
            $right = $mid - 1;
    }
    return -1;
}

echo search([-1,0,2,5,6,8,9,14,20], 9);
echo search([-1,0,2,5,6,8,14,20], 9);
echo search([-1], 9);
echo search([9], 9);
echo search([1,7], 9);
echo search([2,5], 2);