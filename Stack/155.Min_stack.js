
var MinStack = function() {
    let stack = []
    let minStack = [Infinity]
    this.stack = stack
    this.minStack = minStack
};

MinStack.prototype.push = function(val) {
    let min = Math.min(val, this.getMin())
};

MinStack.prototype.pop = function() {

};

MinStack.prototype.top = function() {

};

MinStack.prototype.getMin = function() {

};

