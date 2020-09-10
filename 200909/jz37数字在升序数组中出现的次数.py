#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        con = 0 
        for i in range(len(data)):
            if data[i] == k:
                con += 1

        return con