
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
    this.minStack.pop()
};

MinStack.prototype.top = function() {
    return this.stack.length ? this.stack[this.stack.length-1] : null
};

MinStack.prototype.getMin = function() {
    return this.minStack.length ? this.minStack[this.minStack.length-1] : null
};

