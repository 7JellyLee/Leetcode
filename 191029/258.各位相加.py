#Leetcode
#258.各位相加
#反复将各个位上的数字相加，直到结果为一位数

#本题关键点
#1.传统递归算法
#2.归纳总结得，当数字为0-9时。结果为它本身；
#  数字大于9且为9的倍数时，结果为9，
#  当数字大于9且不是9的倍数时，结果为该数mod 9的余数
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        sum = 0
        while num:
            sum += num % 10
            num = num // 10

        return self.addDigits(sum)

     #方法二：0（1）的做法
     def addDigits(self, num: int) -> int:
        if num < 9:
            return num
        elif num % 9:
            return num % 9
        else:
            return 9


