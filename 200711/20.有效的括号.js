// Leetcode
// 20.有效的括号

// 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

// 本题关键点
// 1.本题是栈类题型，栈是先进后出的，题目列举3对6种符号，可进行一一列举
// 2.JavaScript语言进栈.push出栈.pop   
// 
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let arr = []
    let len = s.length
    if (len % 2) return false
    for (let i = 0; i < len; i++) {
        let letter = s[i]
        switch (letter) {
            case "(":
                {
                    arr.push(letter)
                    break;
                }
            case "[":
                {
                    arr.push(letter)
                    break;
                }
            case "{":
                {
                    arr.push(letter)
                    break;
                }
            case ")":
                {
                    if (arr.pop() !== "(") return false
                    break;
                }
            case "]":
                {
                    if (arr.pop() !== "[") return false
                    break;
                }
            case "}":
                {
                    if (arr.pop() !== "{") return false
                    break;
                }
        }
    }
    return !arr.length
};