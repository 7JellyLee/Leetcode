#Leetcode
#283.移动零
# 编写一个函数，将数组nums中的0全部一定到数组的末尾，同时保持非零元素的相对位置

#本题关键点
#1.遍历数组，k记录
# 2.数组多个赋值 nums[k:] = [0] * (个数)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         k = -1

            for num in nums:
                if num :
                    k += 1
                    nums[k] = num
                else:
                    continue

            if k == len(nums):
                return nums
            else:
                nums[k+1:] = [0] * (len(nums) - k - 1)
