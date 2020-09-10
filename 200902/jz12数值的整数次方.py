#题目描述
#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, x, n):
        # write code here
        if x == 0:
            if n < 0:
                return 
            else:
                return 0
            
        t = abs(n)
        res = 1.0
        
        while t:
            res *= x
            t -= 1
        
        if n < 0:
            res = 1 / res
        
        return res
            