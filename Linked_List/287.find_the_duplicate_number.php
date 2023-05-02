<?php

function findDuplicate($nums)
{
  $slow = $slow2 = $fast = 0;
  while (true) {
    $slow = $nums[$slow];
    $fast = $nums[$nums[$fast]];
    if ($slow === $fast)
      break;
  }
  while (true) {
    $slow = $nums[$slow];
    $slow2 = $nums[$slow2];
    if ($slow === $slow2)
      return $slow;
  }
}
