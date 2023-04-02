<?php

function isValid($s) {
    $len = strlen($s);
    $match = [
        ')' => '(',
        ']' => '[',
        '}' => '{'
    ];
    $stack = [];
    for ($i=0; $i<$len; $i++){
        if ($i === 0 && isset($match[$s[$i]]))
            return false;
        if (!isset($match[$s[$i]]))
            $stack[] = $s[$i];
        else if ( array_pop($stack) !==  $match[$s[$i]] )
            return false;
    }
}


echo 'false > ',isValid('('),"\n";
echo 'false > ',isValid(')('),"\n";
echo 'false > ',isValid('(]'),"\n";
echo 'false > ',isValid('(}'),"\n";
echo 'false > ',isValid('([)]'),"\n";
echo 'false > ',isValid('(('),"\n";
echo 'true > ',isValid('([])'),"\n";
echo 'true > ',isValid('([{{}}[]])'),"\n";
echo 'true > ',isValid('()'),"\n";
echo 'true > ',isValid('()[]{}'),"\n";