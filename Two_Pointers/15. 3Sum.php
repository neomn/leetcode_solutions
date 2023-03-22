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
        while ($left < $right) {
            $sum = $nums[$i] + $nums[$left] + $nums[$right];
            if ($sum < 0)
                $left++;
            elseif ($sum > 0)
                $right--;
            else {
                $result[] = array($nums[$i], $nums[$left], $nums[$right]);
                while ($left < $right && $nums[$left] == $nums[$left + 1])
                    $left++;
                while ($left < $right && $nums[$right] == $nums[$right - 1])
                    $right--;
                $left++;
                $right--;
            }
        }
    }
    return $result;
}

$nums = [-5,-8,-15,54,0,5,3,-7,1,0,2,43,-1,12,-3,0,6,1,9];
print_r( threeSum($nums) );