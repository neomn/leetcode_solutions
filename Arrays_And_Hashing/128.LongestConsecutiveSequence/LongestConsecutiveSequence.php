<?php

function longestConsecutive($nums) {
    $set = array_flip($nums);
    $longestLength = 0;
    foreach ($nums as $num) {
        if (!isset($set[$num-1])) {

        }
    }
}

print_r(longestConsecutive([0,3,7,2,5,8,4,6,0,1]));