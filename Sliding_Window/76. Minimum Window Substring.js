
const minWindow = function(s, t) {
    let mapT = {}, len = t.length, result = [], min = Infinity;
    for (let char of t)
        mapT[char] = (mapT[char] || 0) + 1;
    for (let right = 0, left = 0; right < s.length; right++) {
        if (mapT[s[right]] > 0) --len
        --mapT[s[right]]
        while (!len) {
            if (right - left < min) {
                min = right - left;
                result = [left, right];
            }
        }
    }
}

console.log(minWindow('ADOBECODEBANC', 'ABC') , ' BANC')