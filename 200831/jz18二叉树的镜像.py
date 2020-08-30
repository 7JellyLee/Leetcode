#题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。即二叉树反转
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param pRoot TreeNode类 
# @return void
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here

        if not pRoot: #若为空树，返回0
            return 

        stack = [pRoot]  #stack 赋值为根结点的值

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

        return pRoot

#使用辅助栈的方法，采用后序遍历的方式，交换每个节点
#其中重要知识点 ： Python 利用平行赋值的写法（即 a, b = b, aa,b=b,a ），可省略暂存操作。其原理是先将等号右侧打包成元组 (b,a)(b,a) ，再序列地分给等号左侧的 a, ba,b 序列。
