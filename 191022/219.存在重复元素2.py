#Leetcode
#219.存在重复元素2
#给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

#本题关键
#不太熟悉字典，还需要再多做多看相关题目
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return 0

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
            dict[nums[i]] = i
        return False

