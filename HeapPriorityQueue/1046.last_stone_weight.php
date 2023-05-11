<?php

function lastStoneWeight($stones)
{
  $heap = new SplMaxHeap();
  foreach ($stones as $stone)
    $heap->insert($stone);
  while ($heap->count() > 1) {
    $y = $heap->extract();
  }
}
