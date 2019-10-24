#Leetcode
#206.反转一个单链表

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        p = head
        
        while p:
            r = p.next
            p.next = dummy
            dummy = p
            p = r
        
        return dummy
            
