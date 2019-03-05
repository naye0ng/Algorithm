"""
1232.사칙연산
"""
import sys
sys.stdin = open('input.txt','r')

class Stack() :
    def __init__(self):
        self.top = -1
        self. stack = []

    def push(self, data):
        self.stack += [data]
        self.top +=1

    def pop(self):
        temp = self.stack[self.top]
        self.stack = self.stack[:self.top]
        self.top -= 1
        return temp

def inorder(t) :
    if t :
        inorder(tree[t][1])
        inorder(tree[t][2])

        if type(tree[t][0]) == int :
            stack.push(tree[t][0])
        else :
            x = stack.pop()
            y = stack.pop()
            if tree[t][0] == '+' :
                stack.push(y+x)
            elif tree[t][0] == '-' :
                stack.push(y-x)
            elif tree[t][0] == '*' :
                stack.push(y*x)
            elif tree[t][0] == '/' :
                stack.push(y//x)

for test_case in range(1,11) :
    N = int(input())
    tree = [ [0]*3 for _ in range(N+1) ]
    for _ in range(N) :
        node = input().split()
        if len(node) == 2 :
            tree[int(node[0])][0] = int(node[1])
        else :
            tree[int(node[0])][0] = node[1]
            tree[int(node[0])][1] = int(node[2])
            tree[int(node[0])][2] = int(node[3])

    stack = Stack()
    inorder(1)

    print('#{} {}'.format(test_case, stack.pop()))