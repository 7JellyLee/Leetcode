#Leetcode
#303.区域和检索-数组不可变

#给定一个数组nums，求数组从索引i到j范围内元素的总和包括i和j两点


#本题关键点
#1

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] = self.nums[i]+self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i>0:
            return self.nums[j]-self.nums[i-1]
        else:
            return self.nums[j]
