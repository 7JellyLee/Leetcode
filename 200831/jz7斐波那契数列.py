#题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。n<=39

#题解 讨论 通过的代码笔记 纠错 收藏
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a , b = 0 , 1

        for _ in range(n):
            a , b = b, a+b
            return a%10000007