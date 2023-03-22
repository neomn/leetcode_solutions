<?php

function maxArea($height) {
    $maxArea = $left = 0;
    $right = $length = count($height)-1;
    while($left<$right){
        if ($height[$left] < $height[$right]){
            $maxArea = max($maxArea, ($height[$left] * $length));
            ++$left;
        }
    }
}

echo maxArea([1,8,6,2,5,4,8,3,7]);