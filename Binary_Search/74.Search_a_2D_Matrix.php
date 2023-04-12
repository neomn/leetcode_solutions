<?php

function searchMatrix($matrix, $target) {
    $left = 0;
    $right = count($matrix[0])-1;
    $down = count($matrix)-1;
    while($left <  $down){
        $middle = floor(($left+$down)/2);
        if ($matrix[$middle][0] <= $target && $target <= $matrix[$middle][$right]){
            $left = $middle;
            break;
        }
        $matrix[$middle][0] > $target ? $down= $middle -1 : $left = $middle + 1;
    }
    $targetRow = $left;
    $left = 0;
    $right = count($matrix[$targetRow])-1;
    if ($matrix[$targetRow][$left] == $target || $matrix[$targetRow][$right] == $target)
        return true;
    while($left <= $right){
        $middle = floor(($right+$left)/2);
        if ($matrix[$targetRow][$middle] == $target)
            return true;
        $matrix[$targetRow][$middle] < $target ? $left = $middle + 1 : $right = $middle - 1;
    }
    return false;
}

echo searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), "\n";
echo searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11), "\n";
echo searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30), "\n";
echo searchMatrix([[1],[2],[3]], 3), "\n";
echo searchMatrix([[3]], 3), "\n";
echo searchMatrix([[-6],[3]], 3), "\n";
echo searchMatrix([[3]], 6), "\n";
