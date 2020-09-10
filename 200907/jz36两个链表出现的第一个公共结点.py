#题目描述
#输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = 0
        len2 = 0

        p1 = pHead1
        p2 = pHead2

        while p1:
            len1 += 1
        while p2 :
            len2 += 1

        if len1 > len2:
            long = pHead1
        else:
            short = pHead1
        
        diff = abs(len1 - len2)

        for i in range(diff):
            long = long.next

        while long:
            if long == short:
                return long
            long = long.next
            short = short.next

        return None