<?php

function isPalindrome($s) {
    $leftPointer = 0;
    $rightPointer = count($s)-1;
    while($leftPointer < $rightPointer){
        if (!ctype_alnum($s[$leftPointer])){
            $leftPointer++;
            continue;
        }
    }
}

$sample = "A man, a plan, a canal: Panama";
echo isPalindrome($sample);