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

  public function getNext()
  {
    return $this->next;
  }

  public function setNext($next)
  {
    $this->next = $next;
  }

  public function toArray()
  {
    $arr = [];
    $cur = $this;
    while ($cur != null) {
      array_push($arr, $cur->val);
      $cur = $cur->next;
    }
    return $arr;
  }

  public static function fromArray($arr)
  {
    $dummy = new ListNode();
    $cur = $dummy;
    foreach ($arr as $val) {
      $cur->next = new ListNode($val);
      $cur = $cur->next;
    }
    return $dummy->next;
  }
}
