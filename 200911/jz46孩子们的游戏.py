#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1

        s = 0

        for i in range(2,n+1):
            s = (s + m) % i
         return s