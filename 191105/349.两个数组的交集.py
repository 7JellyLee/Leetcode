#Leetcode
#349.两个数组的交集

#给定两个数组，编写一个函数来计算他们的交集

#本题关键点
# 1.python操作 x & y交集
# 2.list函数将元组转化为列表
# 3.set无序不重复函数
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
