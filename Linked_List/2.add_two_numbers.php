<?php

function addTwoNumbers($l1, $l2)
{
  $resutl = new ListNode();
  $temp = $result;
  $carry = 0;
  while ($l1 || $l2 || $carry) {
    $sum = ($l1 ? $l1->val : 0) + ($l2 ? $l2->val : 0) + $carry;
    $carry = 0;
    if ($sum > 9) {
      $carry = 1;
      $sum -= 10;
    }
    $temp->val = $sum;
    $l1 = $l1 ? $l1->next : null;
    $l2 = $l2 ? $l2->next : null;
    if ($l1 || $l2 || $carry) {
      $temp->next = new ListNode();
      $temp = $temp->next;
    }
  }
}
