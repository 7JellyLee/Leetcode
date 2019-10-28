#Leetcode
#242.有效的字母异位词
#给定两个字符串s和t，判断s是否是t的字母异位词

#本题关键点
#1.本题其实就是考察是判断st两个字符串相同的字母出现次数是否相同。
#2.利用哈希表，遍历s字符串，字母出现index加1，遍历t字符串，字母不在字典中就返回错误，字母出现index减1。
# 最后看，字典中对应的index是否都为0，是就返回正确，不是返回错误。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for i in t:
            if i not in dict or dict[i] <= 0:
                return False
            dict[i] -= 1

        for i in dict:
            if dict[i] != 0:
                return False

        return True
