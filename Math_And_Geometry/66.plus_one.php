<?php

function plusOne($digits)
{
  $n = count($digits);
  for ($i = $n - 1; $i >= 0; $i--) {
    $digits[$i]++;
  }
}
