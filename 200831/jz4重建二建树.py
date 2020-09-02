#题目描述
#输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# -*- coding:utf-8 -*-
class Solution:
    # 返回构造的TreeNode根节点
    def buildTree(self, preorder, inorder):
        if not preorder or inorder:
            return 

        root  = TreeNode(preorder[0])
        i = inorder.index(root)
        left_nodes = inorder[:i]
        right_nodes = inorder[i + 1 :]
        root.left = self.buildTree(preorder[1:i+1],left_nodes)
        root.right = self.buildTree(preorder[i+1:],right_nodes)
        
        return root