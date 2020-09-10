#题目描述
# 统计一个数字在升序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    

    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0

        dLeft = self.TreeDepth(pRoot.left)
        dRight = self.TreeDepth(pRoot.left)
        
        return max(dLeft, dRight) + 1 