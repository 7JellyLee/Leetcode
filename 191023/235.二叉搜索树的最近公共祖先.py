#Leetcode
#235.二叉搜索树的最近公共祖先
#一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先

#本题关键点
#1.利用二叉搜索树的性质，根节点的值大于左子树小于右子树。
#2.同时本题使用递归算法
#3.如果p,q都小于root的值，说明都在左子树上，而且root不是最近共同节点，就递归左子树。
#4.同理如果都大于root的值，就递归右子树。
#5.如果p或者q在递归过程中就是根节点，直接返回p，q即可。
#6.如果是其中一个小于root另一个大于root的值，说明root就是p，q的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        if root == p:
            return p
        if root == q:
            return q

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root



