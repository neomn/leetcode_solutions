<?php

function topKFrequent($nums, $k){
    $frequencyArray = array();
    $heap = new SplMaxHeap();
    foreach($nums as $key => $input)
        !isset($frequencyArray[$input]) ? $frequencyArray[$input] = 0 : $frequencyArray[$input]++;

    foreach ($frequencyArray as $num => $repeatedTimes )
        $heap->insert([$repeatedTimes, $num]);

    $result = array();
    for( $i=0; $i<$k; $i++ )
        $result[] = $heap->extract()[1];

    return $result;
}