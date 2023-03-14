<?php

//function productExceptSelf($nums) {
//    $output = array();
//    foreach($nums as $key => $num)
//        $key !== 0 ? $output[$key] = $output[$key-1] * ($nums[$key-1]): $output[$key] = 1;
//
//    $postProducts = 1;
//    foreach($nums as $key => $num){
//        $reversedKey = count($nums)-$key-1;// start foreach from the end of the array
//        if ($reversedKey !== count($nums)-1){
//            $postNumber = $nums[$reversedKey+1];
//            $postProducts *= $postNumber;
//        }
//        $output[$reversedKey] *= $postProducts;
//    }
//    return $output;
//}



function productExceptSelf($nums) {
    $numsCount = count($nums);
    $output = array_fill(0, $numsCount, 1);
    $preProducts = 1;
    $postProducts = 1;

    for ($i = 0; $i < $numsCount; $i++) {
        $output[$i] *= $preProducts;
        $preProducts *= $nums[$i];

        $reversedIndex = $numsCount - $i - 1;
        $output[$reversedIndex] *= $postProducts;
        $postProducts *= $nums[$reversedIndex];
    }

    return $output;
}


print_r(productExceptSelf(  [1,2,3,4]  ));