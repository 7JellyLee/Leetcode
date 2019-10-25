#Leetcode
#226.翻转二叉树
#反转一棵二叉树


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root != None:
            node = root
            node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        else:
            return None

        return node
