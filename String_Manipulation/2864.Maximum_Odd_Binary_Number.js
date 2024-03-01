/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    let c = s.split("1").length-1
    return "1".repeat(c-1) + "0".repeat(s.length-c) + "1"
};
