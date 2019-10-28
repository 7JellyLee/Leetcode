#Leetcode
#234.回文链表
#判断一个链表是否是回文链表

#本题关键点
#1.回文链表将一半链表逆转，再比较前后两个部分是否相等
#2.用快慢指针找到链表的中间点，快指针每次移动两个节点，慢指针移动一个节点。
# 当快指针到链表结尾时，慢指针此时就在链表中间位置，其中要注意链表节点的奇偶数，奇数慢指针需要指向下一个节点。
# 3.翻转链表代码

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next == None:
            if head.val == head.next.val:
                return True
            else:
                return False

        fast = head.next.next
        slow = head.next

        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        prep = p = None

        while head != slow:
            p = head.next
            head.next = prep
            prep = head
            head = p

        if fast is not None and fast.next is None:
            slow = slow.next

        while(prep is not None):
            if prep.val != slow.val:
                return False
            prep = prep.next
            slow = slow.next
        return True
