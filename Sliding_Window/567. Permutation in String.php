<?php

function checkInclusion($s1, $s2){
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
            if (isset($requiredChars[$s2[$i]]))
                --$requiredChars[$s2[$i]];
            else isset($buffer[$s2[$i]]) ? ++$buffer[$s2[$i]] : $buffer[$s2[$i]] = 1;
            if (isset($requiredChars[$s2[$i]]) && $requiredChars[$s2[$i]] === 0)
                unset($requiredChars[$s2[$i]]);
        }
    }
}

echo checkInclusion('ab',   'eidbaooo') ,     'true',"\n";


