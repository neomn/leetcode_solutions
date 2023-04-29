<?php

function addTwoNumbers($l1, $l2)
{
  $resutl = new ListNode();
  $temp = $result;
  $carry = 0;
  while ($l1 || $l2 || $carry) {
    $sum = ($l1 ? $l1->val : 0) + ($l2 ? $l2->val : 0) + $carry;
  }
}
