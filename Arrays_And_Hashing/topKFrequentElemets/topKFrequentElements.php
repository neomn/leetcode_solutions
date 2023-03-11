<?php

function topKMostFrequentElements($inputArray, $K){
    $frequencyArray = array();
    $heap = new SplMinHeap();
    $result = array();
    foreach($inputArray as $key => $input){
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;

    }

}