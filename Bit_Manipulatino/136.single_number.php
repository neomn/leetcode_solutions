<?php

function singleNumber($nums)
{
  foreach ($nums as $num)
    $result ^= $num;
}
