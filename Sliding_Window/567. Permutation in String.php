<?php

function checkInclusion($s1, $s2)
{
    $hashmap = $buffer = $requiredChars = [];
    $lenS1 = strlen($s1);
    $lenS2 = strlen($s2);
    $left = 0;
    if ($lenS1 > $lenS2)
        return false;

    for ($i = 0; $i < $lenS1; $i++) {
        if ($s1[$i] !== $s2[$i]) {
            isset($hashmap[$s1[$i]]) ? ++$hashmap[$s1[$i]] : $hashmap[$s1[$i]] = 1;
            isset($requiredChars[$s1[$i]]) ? ++$requiredChars[$s1[$i]] : $requiredChars[$s1[$i]] = 1;

        }
    }
}



