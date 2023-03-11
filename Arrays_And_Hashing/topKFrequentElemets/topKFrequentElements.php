<?php

function topKFrequent($nums, $k){
    $frequencyArray = array();
    $heap = new SplMinHeap();
    foreach($nums as $key => $input)
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;

    foreach ($frequencyArray as $num => $repeatedTimes ){
        $heap->insert([$repeatedTimes, $num]);
        if ($heap->count() > $k)
            $heap->extract();
    }

    $result = array();
    while(!$heap->isEmpty())
        $result[] = $heap->extract()[1];

    return $result;
}