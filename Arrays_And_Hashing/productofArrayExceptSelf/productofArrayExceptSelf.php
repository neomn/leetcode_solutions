<?php

function productExceptSelf($nums) {
    $output = array();
    foreach($nums as $key => $num){
//        $preProducts = 1;
//        if ($key !== 0)
//            $preProducts = $output[$key-1] * ($nums[$key-1]);
//        $output[$key] = $preProducts;

        $key !== 0 ? $output[$key] = $output[$key-1] * ($nums[$key-1]): $output[$key] = 1;
    }
    print_r($output);
    echo "\n";
    echo "\n";


    foreach($nums as $key => $num){
        $reversedKey = count($nums)-$key-1;// start foreach from the end of the array
        $postProducts = 1;
        print_r($reversedKey);
        if ($reversedKey !== count($nums)-1)
            $postProducts = $output[$reversedKey+1] * ($nums[$reversedKey+1]);
        $output[$reversedKey] *= $postProducts;
        print_r($postProducts);
        echo "\n";
    }
//    return $output;
}

print_r(productExceptSelf(  [1,2,3,4]  ));