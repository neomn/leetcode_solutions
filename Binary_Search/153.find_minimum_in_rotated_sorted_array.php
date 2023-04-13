<?php

function findMin($nums){
    $l = 0;
    $r = count($nums) - 1;
    if ($nums[$l] < $nums[$r] || !isset($nums[1]))
        return $nums[0];
}

echo findMin([3,4,5,1,2]), "\n";
