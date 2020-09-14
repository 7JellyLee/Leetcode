#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, array, tsum):
        res = []
        min_x = float('inf')

        for i in range(len(array)):
            t = tsum - array[i]
            if t in array[i+1]:
                temp = t * array[i]
                if temp < min_x:
                    min_x = temp
                    res = [array[i], t]
        return res
