"""
4874.Forth
"""
class Stack :
    def __init__(self):
        self.top = -1
        self.stack = [0]*256
    
    def push(self,value) :
        self.top +=1
        self.stack[self.top] =int(value)

    def pop(self) :
        value = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -=1
        return value

T = int(input())
for test_case in range(1,T+1):
    
    inputData = input().split()

    result = "error"
    stack = Stack()

    for data in inputData :
        if data == '.' :
            if stack.top == 0 :
                result = stack.pop()
            break

        if data == '+' :
            if stack.top < 1:
                break
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(val1+val2)
        elif data == '-' :
            if stack.top < 1:
                break
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(val2-val1)
        elif data == '*' :
            if stack.top < 1:
                break
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(val1*val2)
        elif data == '/' :
            if stack.top < 1:
                break
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(val2//val1)
        else :
            # 숫자인 경우
            stack.push(int(data))

    print(f'#{test_case} {result}')