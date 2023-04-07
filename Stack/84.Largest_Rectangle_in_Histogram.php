<?php

function largestRectangleArea($heights) {
    $maxArea = 0;
    $stack = [];
    $heights[] = 0;
    for ($i = 0; $i < count($heights); $i++) {
        while ( $stack && $heights[$i] < $heights[end($stack)]) {
            $h = $heights[array_pop($stack)];
            $w = !$stack ? $i : $i - end($stack) - 1;
            $maxArea = max($maxArea, ($h * $w));
        }
        $stack[] = $i;
    }
    return $maxArea;
}

largestRectangleArea([2,4]);

