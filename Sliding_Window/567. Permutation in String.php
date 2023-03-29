<?php

function checkInclusion($s1, $s2){
    $hashmap = $buffer = $requiredChars = [];
    $lenS1 = strlen($s1);
    $lenS2 = strlen($s2);
    $matches = 0;
    $mapS1 = $mapS2 = array_fill(0,26,0);
    for ($i=0; $i<$lenS1; $i++){
        ++$mapS1[ord($s1[$i]) - ord('a')];
        ++$mapS2[ord($s2[$i]) - ord('a')];
    }
    for ($i=0; $i<26; $i++)
        if ($mapS1[$i] === $mapS2[$i])
            ++$matches;
    $left = 0;

}



//echo checkInclusion('ab',   'eidbaooo') ,     'true',"\n";
//echo checkInclusion('ab',   'eidboaooo') ,     'false',"\n";
//echo checkInclusion('abac', 'eidbaooo') ,     'false',"\n";
echo checkInclusion('adc',  'dcda') ,         'true',"\n";
//echo checkInclusion('ab',   'ab') ,           'true',"\n";
//echo checkInclusion('abca', 'ccccbbbbaaaa') , 'false',"\n";


