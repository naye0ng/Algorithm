"""
4866.괄호검사
"""
T = int(input())
for test_case in range(1, T + 1):

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

    s = Stack()
    result = 1

    for a in input().replace(""," ").split() :
        print(a)
        if a == '(' or a == '{' :
            s.push(a)
            
        if a == ')' :
            if s.top == -1  or s.pop() != '(' :
                result = 0
                break
        elif a == '}' :
            if s.top == -1 or s.pop() != '{' :
                result = 0
                break

    if s.top != -1 :
        result = 0

    print(f'#{test_case} {result}')