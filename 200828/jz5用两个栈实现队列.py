#题目描述
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution:
    def __init__(self):
        self.stack1 = []  #初始化两个栈
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)  #stack1负责入栈操作

    def pop(self):
        if self.stack2 == []: #如果stack2为空则将stack1数据转移到stack2，再pop stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  #如果stack2不为空则可直接pop