#Leetcode
#231.2的幂
#给定一个整数，判断是否是2的幂次方


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
