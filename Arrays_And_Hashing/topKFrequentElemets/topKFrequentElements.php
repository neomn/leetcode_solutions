<?php

function topKFrequent($nums, $k){
    $frequencyArray = array();
    foreach($nums as $num)
        !isset($frequencyArray[$num]) ? $frequencyArray[$num] = 1 : $frequencyArray[$num]++;

    $buckets = array_fill(0, count($nums) + 1, array());
    foreach($frequencyArray as $num => $freq)
        $buckets[$freq][] = $num;

    $result = array();
    for($i = count($buckets) - 1; $i >= 0 && count($result) < $k; $i--)
        if(!empty($buckets[$i]))
            $result = array_merge($result, $buckets[$i]);

    return $result;
}


