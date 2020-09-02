#题目描述
#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 1:
            return 1

        return 2 * self.jumpFloorII(number -1)  #根据公式推导，f(n) =  2 * f(n - 1) 


#本题是动态规划 动态规划经典 f（n） = f(n-1) + f(n-2) + b