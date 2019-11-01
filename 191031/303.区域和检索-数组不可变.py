#Leetcode
#303.区域和检索-数组不可变

#给定一个数组nums，求数组从索引i到j范围内元素的总和包括i和j两点


#本题关键点
#1

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        hash_p = {}
        hash_w = {}

        if len(words) != len(pattern):
            return False

        for i,letter in enumerate(pattern):
            if hash_p.get(letter):
                if hash_p[letter] != words[i]:
                    return  False
            else:
                hash_p[letter] = words[i]

        for i, word in enumerate(words):
            if hash_w.get(word):
                if hash_w[word] != pattern[i]:
                    return False
            else:
                hash_w[word] = pattern[i]

        return True
