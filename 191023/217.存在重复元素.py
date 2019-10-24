#Leetcode
#217.存在重复元素
#如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。


#set函数
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for i in nums:
            if i in nums1:
                return True
            else:
                nums1.add(i)
        return False

