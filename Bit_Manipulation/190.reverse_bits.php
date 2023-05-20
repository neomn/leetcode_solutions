<?php

function reverseBits($n)
{
  $ans = 0;
  for ($i = 0; $i < 32; $i++) {
    $ans <<= 1;
    $ans |= ($n & 1);
  }
}
