<?php

function topKMostFrequentElements($inputArray, $K){
    $frequencyArray = array();
    $heap = new SplMinHeap();
    foreach($inputArray as $key => $input){
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;
        $heap->insert([$frequencyArray[$input], $input]);
        if ($heap->count() > $K)
            $heap->extract();
    }
    $result = array();
    while( !$heap->isEmpty() )
        $result[] = $heap->extract()[1];

    return $result;
}