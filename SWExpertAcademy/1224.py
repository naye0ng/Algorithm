"""
1224.계산기3
"""
class Stack :
    def __init__(self) :
        self.stack = [0]*n
        self.top = -1

    def push(self, value) :
        self.top +=1
        self.stack[self.top] = value
    
    def pop(self) :
        value = self.stack[self.top] 
        self.stack[self.top] = 0
        self.top -=1
        return value

for test_case in range(1,11) :
    n = int(input())

    inputData = input().replace(""," ").split()

    oper = Stack()
    num = Stack()

    # 후위표현식으로 변환
    for data in inputData :
        # 정수라면
        if 48 <= ord(data) and ord(data)<=57 :
            num.push(int(data))
        elif data == ')' :
            # '('나올때까지 계속 pop
            while 1 :
                if oper.stack[oper.top] == '(' :
                    # 괄호 빼주기
                    oper.pop()
                    break
                op = oper.pop()
                
                val1 = num.pop()
                val2 = num.pop()
                if op == '+' :
                    num.push(val1+val2)
                elif op == '*' :
                    num.push(val1*val2)
            
        # 연산자나 여는 괄호가 나온다면
        else :
            if data == '+' :
                while 1 :
                    if oper.top== -1 or oper.stack[oper.top] == '(' :
                        break
                    op = oper.pop()
                    # num.push(op)
                    val1 = num.pop()
                    val2 = num.pop()
                    if op == '+' :
                        num.push(val1+val2)
                    elif op == '*' :
                        num.push(val1*val2)
            oper.push(data)

    # 남아있는 연산자 빼기
    while oper.top != -1 :
        # num.push(oper.pop())
        op = oper.pop()
        val1 = num.pop()
        val2 = num.pop()
        if op == '+' :
            num.push(val1+val2)
        elif op == '*' :
            num.push(val1*val2)

    print(f'#{test_case} {num.stack[0]}')
    




