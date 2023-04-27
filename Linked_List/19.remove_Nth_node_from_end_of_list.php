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

  while ($head->next) {
    $temp = $temp->next;
    $head = $head->next;
  }
  $temp->next = $temp->next->next;
}
