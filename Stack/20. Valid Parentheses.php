<?php

function isValid($s) {


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