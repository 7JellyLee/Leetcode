#题目描述
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        
        if not pHead or not pHead.next:
            return None 

        pSlow = pHead
        pFast =  pHead

        while True:
            pSlow = pSlow.next
            pFast = pFast.next.next

            if pSlow == pFast:
                p1 = pFast
                p2 = pHead
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1