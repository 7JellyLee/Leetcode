#Leetcode
#344.反转字符串
#原地修改输入数组，将输入的字符串反转过来

#本题关键点
#1. 本题使用双指针交换
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        if l < 2:
            return s

        j = l - 1
        i = 0

        while i < j:
            s[i], s[j] = s[j],s[i]
            i += 1
            j -= 1
        return s
