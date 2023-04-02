<?php

function isValid($s) {
    $len = strlen($s);
    $match = [
        ')' => '(',
        ']' => '[',
        '}' => '{'
    ];

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