#Leetcode
#226.翻转二叉树
#反转一棵二叉树

#本题关键点
#递归思想

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        else:
            node = root
            tmp = node.left
            node.left = self.invertTree(node.right)
            node.right = self.invertTree(tmp)
        return node


