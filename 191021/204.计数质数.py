#Leetcode
#204.计数质数
#统计所有小于非负整数n的质数个数

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
