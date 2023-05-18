<?php

class Solution
{
  private $nums;
  private $result = [];
  private $count;

  function subsets($nums)
  {
    $this->nums = $nums;
    $this->count = count($nums);
    $this->helper([]);
    return $this->result;
  }
}
