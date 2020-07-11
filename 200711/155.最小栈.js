// Leetcode
// 155. 最小栈

// 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

// push(x) —— 将元素 x 推入栈中。
// pop() —— 删除栈顶的元素。
// top() —— 获取栈顶元素。
// getMin() —— 检索栈中的最小元素。

// #本题关键点
/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.list = []
    this.length = 0
    this.minList = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.list[this.length] = x
    let min = this.length > 0 ? this.minList[this.length - 1] : Infinity
    this.minList[this.length] = min > x ? x : min
    this.length++
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.list.length = --this.length
    this.minList.length = this.length
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.list[this.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minList[this.length - 1]
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */