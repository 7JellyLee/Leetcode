#Leetcode
#198.打家劫舍
#如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

#本题关键点
#1.本题是典型的动态规划算法题，关键在于找题目的状态转移公式.
#2.状态转移公式为 dp[i] = max(dp[i - 2 ] + nums[i - 1],dp[i-1])(nums索引是从0开始，所以加上的是nums[i - 1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        dp[1] = nums[0]

        for i in range(2,n + 1):
            dp[i] =  max(dp[i-2 ] + nums[i - 1],dp[i-1])

        return dp[-1]

