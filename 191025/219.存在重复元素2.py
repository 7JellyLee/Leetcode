#Leetcode
#219.存在重复元素2
#给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 判断存在重复元素的索引之差小于某个数
        # 先判断 nums [i] = nums [j]
        # 然后判断索引值是否相等，所以索引值可以用 map 存起来

        size = len(nums)
        if size == 0:
            return False

        map = dict()
        for i in range(size):
            if nums[i] in map and i - map[nums[i]] <= k:
                # 只要找到 1 个符合题意的就返回
                return True
            # 更新为最新的索引，这里有贪心选择的思想，索引越靠后，符合题意的数据对的存在性就越大
            map[nums[i]] = i
        # 遍历完成以后，都没有符合题意的时候，才返回 False
        return False
