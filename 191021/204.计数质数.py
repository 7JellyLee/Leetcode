#Leetcode
#204.计数质数
#统计所有小于非负整数n的质数个数

#本题关键点
#1.素数遍历范围不需要从2到n，到根方n就可以
#   range(2,int(n ** 0.5) + 1)
#2.判断素数使用厄拉多塞筛法，即找出一个素数，它的倍数都直接设置为0，排除素数
#   list[i*i:n:i] = [0] * len(list[i*i:n:i])
#（python列表双冒号，分别表示起点终点步长）

class Solution:
    def countPrimes(self, n: int) -> int:
        #2是最小的素数
        if n < 2:
            return 0

        #声明n长度的数组，初始化为1，0 1 不是素数，设置为0
        list = [1] * n
        list[0] = list[1] = 0


        for i in range(2,int(n ** 0.5) + 1):
            list[i*i : n : i] = [0] * len(list[i*i : n : i])

        return sum(list)

