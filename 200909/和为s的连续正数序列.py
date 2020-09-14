#题目描述
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        
        res = []
        i = 1
        j = 2

        while i < j and j < tsum:
            csum = (i + j)*(j-i+1)/2
            if csum < tsum:
                j += 1
            elif csum > tsum:
                i += 1
            else:
                res.append(range(i, j+1))