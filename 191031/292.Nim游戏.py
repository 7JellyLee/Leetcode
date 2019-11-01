#Leetcode
#292.Nim游戏

#两个人玩Nim游戏，桌上又一堆石头，轮流拿掉1-3块石头，拿到最后一块石头人是获胜者，作为先手，来判断是否可以在给定的情况下赢得游戏


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
