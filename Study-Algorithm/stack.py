"""
Stack

- 관련문제 : 4866.py
"""
class Stack :
    def __init__(self):
        self.top = -1
        self.stack = []
    
    def pop(self) :
        value = self.stack[self.top]
        self.top -= 1
        self.stack = self.stack[:-1]
        return value
    def push(self, value) :
        self.stack+=[value]
        self.top +=1
