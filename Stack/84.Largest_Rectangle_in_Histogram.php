<?php

function largestRectangleArea($heights) {
    $maxArea = 0;
    $stack = [];
    $heights[] = 0;
    for ($i = 0; $i < count($heights); $i++) {
        while ( $stack && $heights[$i] < $heights[end($stack)]) {

        }
    }
}

largestRectangleArea([2,4]);

