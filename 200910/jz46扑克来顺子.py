#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, nums):
        # write code here
        if not nums:
            return False
        
        repeat = set()
        ma = 14
        mi = 0

        for num in range(nums):
            if num in repeat:
                return False
            if num == 0:
                continue

            ma = max(ma,num)
            mi = min(mi,num)

            repeat.add(num)

        return ma - mi < 5

                 