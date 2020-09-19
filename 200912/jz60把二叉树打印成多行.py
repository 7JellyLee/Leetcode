#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None

        ls = [pNode]
        res = []

        while ls:
            temp = []
            loop = len(ls)
            for i in range(loop):
                cur = ls.pop(0)
                temp.append(cur.val)

                if cur.left:
                    ls.append(cur.left)
                if cur.right:
                    ls.append(cur.right)

            res.append(temp)
        
        return res
