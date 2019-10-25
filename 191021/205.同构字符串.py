#Leetcode
#205.同构字符串给定两个字符串s和t，判断它们是否是同构的。
#如果s中的字符可以被替换得到t，那么这两个字符串是同构的。
#所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

#本题关键点
#1.同构表示两个字符串的每个位置上字符在自身第一次穿出现的索引是相同的
#2.str可以返回字符串第一次出现所在的索引
# map(函数，可迭代对象) 将会对（参数2：可迭代对象）中的每个元素运用（参数1：函数）并将结果按顺序储存在一个迭代器中，返回这个迭代器
# 使用 [*……] 可对对象解包，本题中 [*map……] 等效于 list(map……)
class Solution:
    def isIsomorphic(self,s:str,t:str) ->bool:
        return [*map(s.index,s)] == [*map(t.index,t)]

#哈希表解法
#不太理解，等后面再看

class Solution:
    def isIsomorphic(self,s:str,t:str) ->bool:
        hash = {}
        for i,c in enumerate(s):
            if hash.get(c):
                if t[i] != hash[c]
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[c] = t[i]
        return True
