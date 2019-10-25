#Leetcode
#206.反转链表
#反转一个单链表

#本题关键点、
#1.链表新建头结点 dummy = None
#2.翻转链表需要三个指针，注意翻转时转换的顺序
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        p = head

        while p is not None:
            r = p.next
            p.next = dummy
            p = r
            
        return dummy
