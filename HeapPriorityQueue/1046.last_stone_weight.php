<?php

function lastStoneWeight($stones)
{
  $heap = new SplMaxHeap();
  foreach ($stones as $stone)
    $heap->insert($stone);
  while ($heap->count() > 1) {
    $y = $heap->extract();
    $x = $heap->extract();
    if ($x != $y)
      $heap->insert($y - $x);
  }
  if ($heap->isEmpty())
    return 0;
}
