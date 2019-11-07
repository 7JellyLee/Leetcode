#Leetcode
#374.猜数字大小
#从1到n选择一个数字。猜错了会告诉这个数字是打了还是小了，调用一个预先定义好的接口guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

#本题关键点
#1.二分查找，难度不大

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            # 猜测结果
            flag = guess(mid)
            if flag == -1:
                # 猜大了
                right = mid - 1
            elif flag == 1:
                # 猜小了
                left = mid + 1
            else:
                # 猜对了
                return mid

