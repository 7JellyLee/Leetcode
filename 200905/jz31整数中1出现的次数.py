#题目描述
#输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        a, b, one_count = 1, 10, 0
        while n >= a:
            x, y = divmod(n, b)
            
            if y >= a * 2:
                one_count += (x + 1) * a
            elif y >= a:
                one_count += y + 1 + (x - 1) * a
            else:
                one_count += x * a 

            a, b = b, b*10 
        
        return one_count
