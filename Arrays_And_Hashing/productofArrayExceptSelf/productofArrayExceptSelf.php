<?php

function productExceptSelf($nums) {
    $output = array();
    foreach($nums as $key => $num)
        $key !== 0 ? $output[$key] = $output[$key-1] * ($nums[$key-1]): $output[$key] = 1;

//    print_r($output);
//    echo "\n";
//    echo "\n";


    $postProducts = 1;
    foreach($nums as $key => $num){
        $reversedKey = count($nums)-$key-1;// start foreach from the end of the array
        $postNumber = 1;
        if ($reversedKey !== count($nums)-1){
            $postNumber = $nums[$reversedKey+1];
            $postProducts *= $postNumber;
        }
        $result = $output[$reversedKey]*$postProducts;

        echo "reversedKey >" . $reversedKey . "\n";
        echo "post number  >" . $postNumber . "\n";
        echo " post product >" . $postProducts. "\n";
        echo " output >" . $output[$reversedKey] . "\n";
        echo " final result >" . $result. "\n";
        echo "\n";
        print_r($output);
        echo "\n";
    }
//    return $output;
}

print_r(productExceptSelf(  [1,2,3,4]  ));