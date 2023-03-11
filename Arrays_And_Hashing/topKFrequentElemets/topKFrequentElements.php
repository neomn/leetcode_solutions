<?php

function topKFrequent($nums, $k){
    $frequencyArray = array();
    $heap = new SplMaxHeap();
    foreach($nums as $key => $input){
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;
        $heap->insert([$frequencyArray[$input], $input]);
    }
    $result = array();
    while( !$heap->isEmpty() )
        $result[] = $heap->extract()[1];

    return $result;
}