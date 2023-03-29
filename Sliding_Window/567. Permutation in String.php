<?php

function checkInclusion($s1, $s2){
    $hashmap = $buffer = $requiredChars = [];
    $lenS1 = strlen($s1);
    $lenS2 = strlen($s2);

    $left = 0;
    if ($lenS1 > $lenS2)
        return false;

    for ($i = 0; $i < $lenS1; $i++) {
        isset($hashmap[$s1[$i]]) ? ++$hashmap[$s1[$i]] : $hashmap[$s1[$i]] = 1;
        if (!isset($requiredChars[$s2[$i]]))
            isset($buffer[$s2[$i]]) ? ++$buffer[$s2[$i]] : $buffer[$s2[$i]] = 1;
        else if ($requiredChars[$s2[$i]] !== 0){
            --$requiredChars[$s2[$i]];
            if ($requiredChars[$s2[$i]] === 0)
                unset($requiredChars[$s2[$i]]);
        }
        if (!isset($buffer[$s1[$i]]))
            isset($requiredChars[$s1[$i]]) ? ++$requiredChars[$s1[$i]] : $requiredChars[$s1[$i]] = 1;
        else if ($buffer[$s1[$i]] !== 0)
            --$buffer[$s1[$i]];
    }
    if (!$requiredChars)
        return true;

    print_r($requiredChars);
}



echo checkInclusion('ab',   'eidbaooo') ,     'true',"\n";
echo checkInclusion('abac', 'eidbaooo') ,     'false',"\n";
echo checkInclusion('adc',  'dcda') ,         'true',"\n";
echo checkInclusion('ab',   'ab') ,           'true',"\n";
echo checkInclusion('abca', 'ccccbbbbaaaa') , 'false',"\n";


