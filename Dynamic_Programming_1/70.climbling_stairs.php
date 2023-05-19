<?php

class Solution
{
  function climbStairs($n)
  {
    return round(pow((1 + sqrt(5)) / 2, $n + 1) / sqrt(5));
  }
}
