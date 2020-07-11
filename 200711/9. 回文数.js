// #Leetcode
// 9. 回文数

// 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

// #本题关键点
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str = x + ""
    let left = 0,
        right = str.length - 1
    while (left < right) {
        if (str[left] != str[right]) return false
        left++
        right--
    }
    return true
};