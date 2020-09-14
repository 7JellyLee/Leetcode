#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):

        res = []

        for num in nums:
            if num not in res:
                res.append(num)
            
            else:
                duplication[0] = num
                return True
        
        return False
