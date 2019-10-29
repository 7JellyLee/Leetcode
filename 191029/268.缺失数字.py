#Leetcode
#268.缺失数字
#给定一个包含0，1，2，，，，n的序列，找出没出现的那个数

#本题关键点
# 1.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in numSet:
                return number
