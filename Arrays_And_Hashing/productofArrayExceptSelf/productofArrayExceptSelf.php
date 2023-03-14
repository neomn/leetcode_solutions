<?php

function productExceptSelf($nums) {
    $numsCount = count($nums);
    $output = array_fill(0, $numsCount, 1);
    $preProducts = 1;
    $postProducts = 1;

    for ($index = 0; $index < $numsCount; $index++) {
        $output[$index] *= $preProducts;
        $preProducts *= $nums[$index];

        $reversedIndex = $numsCount - $index - 1;
        $output[$reversedIndex] *= $postProducts;
        $postProducts *= $nums[$reversedIndex];
    }

    return $output;
}


print_r(productExceptSelf(  [1,2,3,4]  ));