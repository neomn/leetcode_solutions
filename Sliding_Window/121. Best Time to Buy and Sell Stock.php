<?php

function maxProfit($prices) {
    $maxProfit = 0;
    $min = $max = $prices[0];
    foreach($prices as $price){
        if ($price<$min)
            $min = $max = $price;
        if ($price>$max)
            $max = $price;
        $maxProfit = max($maxProfit, ($max-$min));
    }
}

echo maxProfit([2,4,1]);