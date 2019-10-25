#Leetcode
#202.快乐数
#正整数，将该数替换为它每个位置上数字的平方和，重复这个过程直到变成1，也可能无限循环变不到1，如果可以变成1，这个数就是快乐数

class Solution:
    def isHappy(self, n: int) -> bool:
        
        while 1:
            sum = 0
            n = str(n)
            for i in n:
                sum = int(i)**2 + sum
            n = sum
            if n == 4:
                return False
            if n == 1:
                return True
