#题目描述
# 输入一个链表，反转链表后，输出新链表的表头。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return pHead

        last = None#指向上一个节点
        while pHead:
            
            p = pHead.next
            
            pHead.next = last
            last = pHead
            pHead = p
        return last