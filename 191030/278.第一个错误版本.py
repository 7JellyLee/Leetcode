#Leetcode
#278.第一个错误的版本
#产品每个版本就是基于前一个版本开发的，所以错误的版本之后的产品都是错误的。找出产品[1，2，3，，，n]中第一个出错的版本

#本题关键点
# 1.使用二分查找算法的思想可以解决该题
# 2.mid值的要注意不能使用(low + high )//2容易溢出
# 3.mid  =  low + (high - low) // 2
class Solution:
    def firstBadVersion(self, n):
        low  = 1
        high = n

        while low < high :
            mid  =  low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
