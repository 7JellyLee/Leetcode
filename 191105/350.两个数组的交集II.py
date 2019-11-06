#Leetcode
#350.两个数组的交集II

#编写一个函数来判断两个函数的交集


#本题关键点
# 1.先将使用sort函数将两个数组排序
# 2.再使用双指针将两个数组的共同元素拿出来，因为已经排好序，所以如果遇到数字不等，则将较小的数字指针向前加一

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        r = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                r.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return r
