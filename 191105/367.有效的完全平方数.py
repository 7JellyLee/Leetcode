#Leetcode
#367.有效的完全平方数
#编写一个函数来判断整数是否是有效的完全平方数，不可以使用任何的库函数。

#本题关键点
#1. 使用暴力求解
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num :
            i += 1
         return i * i == num
