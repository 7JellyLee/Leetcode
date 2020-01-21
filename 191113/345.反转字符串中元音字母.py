#Leetcode
#345.反转字符串中元音字母

#编写一个函数，以字符串作为输入，反转字符串中的元音字母

#本题关键点
#1.使用前后双指针，如果指针指向的字母不是元音字母前指针后移后指针前移，当两者都是愿元音字母时交换
# 2.元音字母要注意有大写字母的情况
# 3.python中可以不用设置临时变量直接将两者交换 x,y = y,x
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        list_s = list(s)

        low, high = 0, len(s) - 1
        while low < high:
            if list_s[high] not in vowels:
                high -= 1
            if list_s[low] not in vowels:
                low += 1
            if list_s[low] in vowels and list_s[high] in vowels:
                list_s[low], list_s[high] = list_s[high], list_s[low]
                low += 1
                high -= 1
        return str(list_s)
