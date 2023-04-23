<?php

class ListNode
{
  public $val;
  public $next;
  function __construct($val = 0, $next = null)
  {
    $this->val = $val;
    $this->next = $next;
  }
}
