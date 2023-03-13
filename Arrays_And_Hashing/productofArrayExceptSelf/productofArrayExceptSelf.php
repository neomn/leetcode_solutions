<?php

function productExceptSelf($nums) {
    $output = array();
    foreach($nums as $key => $num){
        $preProducts = 1;
        if ($key !== 0)
            $preProducts = $output[$key-1] * ($nums[$key-1]);
        $output[$key] = $preProducts;
    }
    foreach($nums as $key => $num){
        $reversedKey = count($nums)-$key-1;// start foreach from the end of the array
        $reversedKey = abs($reversedKey);
        $postProducts = 1;
        print_r($reversedKey);
//        if ($reversedKey !== count($nums)-1)
//            $postProducts = $output[$key-1] * ($nums[$key-1]);
//        $output[$key] *= $postProducts;
    }
//    return $output;
}

print_r(productExceptSelf(  [1,2,3,4]  ));