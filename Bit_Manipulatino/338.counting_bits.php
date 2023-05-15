<?php

function countBits($n)
{
  $dp = [0];
  $offset = 1;
  for ($i = 1; $i <= $n; $i++) {
    $dp[$i] = $dp[$i - $offset] + 1;
  }
}
