#Leetcode
#257.二叉树的所有路径
#给定一个二叉树，返回所有从根节点到叶子节点的路径

#本题关键点
#1.使用递归，如果是叶子节点，就放在路径结尾，并返回答案。
# 如果不是叶子节点就递归
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            path += str(root.val)
            if not root.left and not root .right:
                path.append(path)
            else:
                path += '->'
                construct_paths(root.left,path)
                construct_paths(root.right,path)

        path = []
        construct paths(root,'')
        return path



