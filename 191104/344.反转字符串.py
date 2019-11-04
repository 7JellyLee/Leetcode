#Leetcode
#344.反转字符串
#原地修改输入数组，将输入的字符串反转过来

#本题关键点
#1.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        res =  [0, 0]
        for x, y in zip(secret, guess):
            if x == y:
                s_c[x] -= 1
                g_c[y] -= 1
                res[0] += 1
        for k in s_c & g_c:
            res[1] += min(s_c[k], g_c[k])
        return "{}A{}B".format(res[0], res[1])
