<?php

function minEatingSpeed($piles, $h) {
    $left = 1;
    $right = $result = max($piles);
    while ($left <= $right){
        $k = floor(($left+$right)/2);
        $HPerK = 0;
        foreach ($piles as $pile)
            $HPerK += ceil($pile/$k);
        if ($HPerK > $h)
            $left = $k + 1;
        else {
            $result = min($result, $k);
        }
    }
}

echo minEatingSpeed([3,6,7,11], 8), "\n";


