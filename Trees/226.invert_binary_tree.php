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
    $this->invert($root->left);
    $this->invert($root->right);
    $temp = $root->left;
    $root->left = $root->right;
    $root->right = $temp;
  }
}
