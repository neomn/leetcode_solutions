<?php

function topKMostFrequentElements($nums, $k){
    $frequencyArray = array();
    $heap = new SplMinHeap();
    foreach($nums as $key => $input){
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;
        $heap->insert([$frequencyArray[$input], $input]);
        if ($heap->count() > $k)
            $heap->extract();
    }
    $result = array();
    while( !$heap->isEmpty() )
        $result[] = $heap->extract()[1];

    return $result;
}