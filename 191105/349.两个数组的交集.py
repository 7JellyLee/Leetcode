#Leetcode
#349.两个数组的交集

#给定一个整数判断是否是3的幂次方

#本题关键点
# 1.迭代循环，只要数字对3除余一直为 0 ，就将n对3取整数
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
