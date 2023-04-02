<?php

function isValid($s) {
    if ( strlen($s)%2 !== 0 )
        return false;

}

echo isValid('('),"\n";
echo isValid('(]'),"\n";
echo isValid('(}'),"\n";
echo isValid('([)]'),"\n";
echo isValid('()'),"\n";
echo isValid('([])'),"\n";
echo isValid('()[]{}'),"\n";