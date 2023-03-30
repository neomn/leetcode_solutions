
const minWindow = function(s, t) {
    let mapT = {}, len = t.length, result = [], min = Infinity;
    for (let char of t)
        mapT[char] = (mapT[char] || 0) + 1;
    for (let right = 0, left = 0; right < s.length; right++) {

    }
}

console.log(minWindow('ADOBECODEBANC', 'ABC') , ' BANC')