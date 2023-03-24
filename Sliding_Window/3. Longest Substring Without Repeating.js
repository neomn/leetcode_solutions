
const lengthOfLongestSubstring = function(s) {
    let max = left = 0
    let container = new Set()
    for (let i=0; i<s.length; i++){
        while (container.has(s[i])) {
            container.delete(s[left])
            ++left
        }
        container.add(s[i])
    }
};

console.log(lengthOfLongestSubstring("abcabcbb"), ' > result shloud be 3')
console.log(lengthOfLongestSubstring("bbbbb"), ' > result shloud be 1')
console.log(lengthOfLongestSubstring("pwwkew"), ' > result shloud be 3')
console.log(lengthOfLongestSubstring(" "), ' > result shloud be 1')
console.log(lengthOfLongestSubstring("au"), ' > result shloud be 2')
console.log(lengthOfLongestSubstring("dvdf"), ' > result shloud be 3')
