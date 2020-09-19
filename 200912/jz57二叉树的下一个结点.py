#题目描述
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None

        if pNode.right:
            p = pNode.right

            while p:
                p = p.left
                return p

        p = pNode
        while True:

            if p.next and p.next.left == p:
                return p.next
            if not p.next:
                return None
            
            p = p.next
            