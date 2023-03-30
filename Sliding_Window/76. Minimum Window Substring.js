
const minWindow = function(s, t) {
    let mapT = {}, len = t.length, result = [], min = Infinity;
    for (let char of t)
        mapT[char] = (mapT[char] || 0) + 1;

}

console.log(minWindow('ADOBECODEBANC', 'ABC') , ' BANC')