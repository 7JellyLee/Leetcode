#Leetcode
#231.2的幂
#给定一个整数，判断是否是2的幂次方

#本题思想
#1.2的幂一般都是1000的格式，所以和n-1与为0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

#2.迭代求解
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
