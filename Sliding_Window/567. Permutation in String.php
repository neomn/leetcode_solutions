<?php

function checkInclusion($s1, $s2){
    $hashmap = $buffer = $requiredChars = [];
    $lenS1 = strlen($s1);
    $lenS2 = strlen($s2);
    $matches = 0;
    $mapS1 = $mapS2 = array_fill(0,26,0);
    $left = 0;

}



//echo checkInclusion('ab',   'eidbaooo') ,     'true',"\n";
//echo checkInclusion('ab',   'eidboaooo') ,     'false',"\n";
//echo checkInclusion('abac', 'eidbaooo') ,     'false',"\n";
echo checkInclusion('adc',  'dcda') ,         'true',"\n";
//echo checkInclusion('ab',   'ab') ,           'true',"\n";
//echo checkInclusion('abca', 'ccccbbbbaaaa') , 'false',"\n";


