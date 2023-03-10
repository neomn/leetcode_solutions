<?php

class Solution
{
    function groupAnagrams($strs)
    {
        $hashmap = [];

        // repeat until strs array get empty
        while (count($strs) > 0) {
            $str = array_pop($strs);

            // generate hashmap key
            if ($str !== ""){
                $splitedStr = str_split($str);
                sort($splitedStr);
                $key = '';
                foreach ($splitedStr as $char) {
                    $charRepeatTimes = substr_count($str, $char);
                    $key .= $char . $charRepeatTimes;
                }
            } else $key = "";

            //iterate through hashmap and compare key with existing keys in hashmap
            $keyNotFound = true;
            foreach (array_keys($hashmap) as $hashmapKey)
                if ($hashmapKey === $key) {
                    echo 'hashmap key matched -> ' . $hashmapKey . ' vs ' . $key . ' for string  ' . $str . "\n";
                    $hashmap[$hashmapKey][] = $str;
                    $keyNotFound = false;
                }

            // if no match found then add new key to the hashmap
            if ($keyNotFound)
                $hashmap[$key] = [$str];
        }
        return $hashmap;
    }
}

$samples = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
    ["",""],
];

$solution = new Solution();
foreach ($samples as $sample) {
    print_r($solution->groupAnagrams($sample));
}
