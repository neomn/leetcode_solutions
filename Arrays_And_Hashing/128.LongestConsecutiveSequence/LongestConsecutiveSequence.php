<?php

function longestConsecutive($nums) {
    $set = array_flip($nums);
    return $set;
}

print_r(longestConsecutive([0,3,7,2,5,8,4,6,0,1]));