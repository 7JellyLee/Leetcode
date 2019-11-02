#Leetcode
#292.Nim游戏

#两个人玩Nim游戏，桌上又一堆石头，轮流拿掉1-3块石头，拿到最后一块石头人是获胜者，作为先手，来判断是否可以在给定的情况下赢得游戏


#本题关键点
# 1.本题代码不难关键在于对题目的理解。
# 2.如果堆中石头的数量 nn 不能被 44 整除，那么你总是可以赢得 Nim 游戏的胜利。
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 != 0:
            return True

        return False
