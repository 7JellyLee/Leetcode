#Leetcode
#299.猜数字
# 你写下一个数字让你的朋友猜，每次他猜测后你给他一个提示，告诉他又多少位数字和确切位置都猜对了称为公牛，有多少数字猜对了但是位置不对称为奶牛，请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

#本题关键点
#1.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         k = -1

            for num in nums:
                if num :
                    k += 1
                    nums[k] = num
                else:
                    continue

            if k == len(nums):
                return nums
            else:
                nums[k+1:] = [0] * (len(nums) - k - 1)
