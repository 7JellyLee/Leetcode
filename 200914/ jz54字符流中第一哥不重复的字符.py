#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = ''
    def FirstAppearingOnce(self):
        res = []

        for i in self.s:
            if i in res:
                res.remove(i)
            else:
                res.append()
    def Insert(self, char):

        self.s += char