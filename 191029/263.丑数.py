#Leetcode
#263.丑数
# 判断一个数是否是丑数，丑数是只包含质因数2，3，5的正整数

#本题关键点
#1.对该数不断除以 2 3 5 ，最后值为1的就是丑数，值不是1的就是不是丑数。
#2.其中很重要的是，对于2的除法，使用移位 >>
class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1 :
            return False

        while num%5 == 0:
            num //= 5
        while num%3 == 0:
            num //= 3
        while num%2 == 0:
            num >>= 1
        if num == 1:
            return True
        else:
            return False
