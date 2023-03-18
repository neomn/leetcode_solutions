<?php

function isPalindrome($s) {
    if (strlen($s)<=1)
        return true;
    $leftPointer = 0;
    $rightPointer = strlen($s)-1;

//    while($leftPointer < $rightPointer){
//
//    }
}

$sample = "A man, a plan, a canal: Panama";
echo isPalindrome($sample);