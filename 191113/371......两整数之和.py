#Leetcode
#371.两整数之和

#不使用运算符+ - ，计算两整数a，b之和


#本题关键点
# 1 python 自带库函数sum求和
# 2.位运算，要注意溢出的问题
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
