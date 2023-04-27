<?php

function removeNthFromEnd($head, $n)
{
  $result = $head;
  $temp = $head;
  while ($n != 0) {
    $head = $head->next;
    --$n;
  }
  if ($head == null)
    return $result->next;
}
