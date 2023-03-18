<?php

function isPalindrome($s) {
    $leftPointer = 0;
    $rightPointer = count($s)-1;
    while($leftPointer < $rightPointer){
        if (!ctype_alnum($s[$leftPointer])){
            $leftPointer++;
            continue;
        }
        if (!ctype_alnum($s[$rightPointer])){
            $rightPointer--;
            continue;
        }
        if (strcmp(strtolower($s[$leftPointer]),strtolower($s[$rightPointer])) !== 0)
            return false;
    }
}

$sample = "A man, a plan, a canal: Panama";
echo isPalindrome($sample);