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

  function helper(array $temp = null, int $counter = 0)
  {
    if ($counter == $this->count) {
      $this->result[] = $temp;
      return;
    }
  }
}
