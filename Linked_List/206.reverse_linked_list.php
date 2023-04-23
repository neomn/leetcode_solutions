<?php

class Solution
{
  function reverseList($head)
  {
  }

  function helper($ref = null, $head)
  {

    //uncomment this if u want to see what's going on
    // echo 'ref > ';
    // var_dump($ref);
    // echo "\n";
    // echo 'head > ';
    // var_dump($head);
    // echo "\n";
    // echo '-----------------------------', "\n";

    if ($head == null)
      return $ref;

    $temp = $head->next;
    $head->next = $ref;
    return $this->helper($head, $temp);
  }
}
