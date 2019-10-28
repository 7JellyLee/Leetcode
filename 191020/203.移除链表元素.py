#Leetcode
#203.移除链表元素元素
#删除链表中等于给定值val的所有节点

#本题关键点
#1.删除元素节点要注意指针变化的顺序
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy .next = head
        prev = dummy
        last = prev.next
        while last :
            if last.val == val:
                prev.next = last.next
                last = prev.next
            else:
                prev = prev.next
                last = prev.next
        return dummy.next
