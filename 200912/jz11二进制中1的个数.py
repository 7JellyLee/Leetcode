#题目描述
#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
class Solution:
    def NumberOf1(self, n):
        n = n & 0xffffffff

        num = 0 
        for i in str(bin(n)):
            if i == '1':
                num += 1

        return num