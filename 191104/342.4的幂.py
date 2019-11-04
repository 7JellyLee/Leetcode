#Leetcode
#342.4的幂

#给定一个整数判断是否是4的幂次方


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
