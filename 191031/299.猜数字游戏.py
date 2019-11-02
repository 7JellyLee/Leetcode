#Leetcode
#299.猜数字
# 你写下一个数字让你的朋友猜，每次他猜测后你给他一个提示，告诉他又多少位数字和确切位置都猜对了称为公牛，有多少数字猜对了但是位置不对称为奶牛，请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

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
