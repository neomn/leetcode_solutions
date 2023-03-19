<?php

function twoSum($numbers, $target) {
    $edgePointerleft = 0;
    $edgePointerRight = count($numbers)-1;
    $middlePointerLeft = floor(count($numbers)/2)-1;
    $middlePointerRight = $middlePointerLeft+1;
    $result = [];
    while (count($result)===0){
        if ($numbers[$edgePointerleft]+$numbers[$edgePointerRight] == $target){
            $result[] = $edgePointerleft+1;
            $result[] = $edgePointerRight+1;
            return $result;
        }
        if ($numbers[$middlePointerLeft]+$numbers[$middlePointerLeft] == $target){
            $result[] = $edgePointerleft+1;
            $result[] = $edgePointerRight+1;
            return $result;
        }
        $numbers[$edgePointerleft]+$numbers[$edgePointerRight] < $target ? $edgePointerleft++ : $edgePointerRight--;
        $numbers[$middlePointerLeft]+$numbers[$middlePointerRight] > $target ? $middlePointerLeft-- : $middlePointerRight++;
    }
}

print_r( twoSum([-19,-12,-6,-4,-3,-1,0,1,6,8,12,16,20],9) );
