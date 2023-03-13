<?php

function productExceptSelf($nums) {
    $output = array();
    foreach($nums as $key => $num){
//        $numsLength = count($nums);
        $preProducts = 1;
        if ($key !== 0)
            $preProducts = $output[$key - 1] * ($nums[$key-1]);
        $output[$key] = $preProducts;
    }
    return $output;
}

print_r(productExceptSelf(  [1,2,3,4]  ));