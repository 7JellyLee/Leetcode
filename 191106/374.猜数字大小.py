#Leetcode
#374.猜数字大小
#从1到n选择一个数字。猜错了会告诉这个数字是打了还是小了，调用一个预先定义好的接口guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

#本题关键点
#1.
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
