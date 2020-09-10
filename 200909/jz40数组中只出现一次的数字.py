#题目描述
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []

        for i in range(len(array)):
            if array.count(i) == 1:
                res.append(i)
        
        return res