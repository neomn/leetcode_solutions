<?php

function isValid($s) {
    do {
       $len = strlen($s);
       $s = str_replace('()','',$s);
       $s = str_replace('{}','',$s);
       $s = str_replace('[]','',$s);
    } while ($len !== strlen($s));
    return strlen($s) === 0;
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