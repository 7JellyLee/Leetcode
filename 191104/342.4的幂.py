#Leetcode
#342.4的幂

#给定一个整数判断是否是4的幂次方


#本题关键点
#1.方法一本题和上题判断3的幂是一样的，循环迭代
# 2.使用位运算，4的幂一定是2的幂，4的幂和2的幂一样，都是只会出现一个1，4的幂总是出现在奇数位上
#  使用num & 0x55555555方式来校验奇数位上的1

class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        while num != 0 and num % 4 == 0:
            num //= 4

        return num == 1


    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and (num & num - 1)==0 and (num & 0x55555555)==num
