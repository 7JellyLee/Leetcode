#Leetcode
#205.同构字符串给定两个字符串s和t，判断它们是否是同构的。
#如果s中的字符可以被替换得到t，那么这两个字符串是同构的。
#所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

class Solution:
    def isIsomorphic(self,s:str,t:str) ->bool:
        return [*map(s.index,s)] == [*map(t.index,t)]
