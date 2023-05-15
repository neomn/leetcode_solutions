<?php

function countBits($n)
{
  $dp = [0];
  $offset = 1;
  for ($i = 1; $i <= $n; $i++) {
    if ($offset * 2 == $i)
      $offset = $i;
    $dp[$i] = $dp[$i - $offset] + 1;
  }
  return $dp;
}
