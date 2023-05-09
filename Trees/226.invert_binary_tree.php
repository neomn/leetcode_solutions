<?php

class Solution
{

  function invertTree($root)
  {
    $this->invert($root);
    return $root;
  }
  function invert($root)
  {
    if (!$root->left && !$root->right)
      return;
  }
}
