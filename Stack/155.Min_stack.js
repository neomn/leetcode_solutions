
var MinStack = function() {
    let stack = []
    let minStack = [Infinity]
    this.stack = stack
    this.minStack = minStack
};

MinStack.prototype.push = function(val) {
    let min = Math.min(val, this.getMin())
    this.stack.push(val)
    this.minStack.push(min)
};

MinStack.prototype.pop = function() {
    this.stack.pop()
};

MinStack.prototype.top = function() {

};

MinStack.prototype.getMin = function() {

};

