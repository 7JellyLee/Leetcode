#Leetcode
#237.删除链表中的节点
#删除某个链表中给定的节点

#本题关键点
#1.本题难点在于题目理解，函数只有一个参数node，没有head，没有其他链表信息。
# 所以使用 替身攻击算法，把下一个节点的值复制到当前节点，然后把下个节点删除即可
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

