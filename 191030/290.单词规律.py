#Leetcode
#290，单词规律
#给定一种规律pattern和一个字符串str，判断str是否完全匹配相同的规律

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
