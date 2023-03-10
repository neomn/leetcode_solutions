<?php

function topKMostFrequentElements($inputArray, $K){
    $inputArrayLength = count($inputArray);
    $heap = new SplMaxHeap();
    $result = array();
    foreach($inputArray as $key => $item){
        echo $item;
    }
}