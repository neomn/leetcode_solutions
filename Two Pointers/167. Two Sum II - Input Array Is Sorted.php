<?php

function twoSum($numbers, $target) {
    $L = 0;
    $R = count($numbers)-1;
    while (true){
        if ($numbers[$L]+$numbers[$R] == $target)
            return [++$L, ++$R];
        $numbers[$L]+$numbers[$R] < $target ? $L++ : $R--;
    }
}

print_r( twoSum([-19,-12,-6,-4,-3,-1,0,1,6,8,12,16,20],9) );
