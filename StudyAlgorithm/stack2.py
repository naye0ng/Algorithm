"""
중위표기법 => 후위 표기법

- 괄호와 연산자용 스택과 피연산자용 스택 총 2개가 필요
- 닫는 괄호가 나오면 자신과 맞는 열린 괄호가 나올때까지 스택에서 빼내기

예). (6+5*(2-8)/2)
    [1]
        ( + * ( - 
        6 5 2 8 

    [2] ) 나오면 ( 나올때까지 빼내기
        ( + *
        6 5 2 8 -

    [3] / 는 *보다 약하고 +보다는 강함, 강한거 빼내고 들어가기
        ( + /
        6 5 2 8 - * 
    
    [4]
        ( + /
        6 5 2 8 - * 2

    [5] ) 나오면 ( 나올때까지 뺴내기
        6 5 2 8 - * 2 / +

예). 7+(5-3*2/1)-4*((4-2)/2+3)+3
    [1] 
        + ( - * 
        7 5 3 2 

    [2] / 는 *보다 약하고 +보다는 강함, 강한거 빼내고 들어가기
        + ( - /
        7 5 3 2 * 1

    [3] ) 나오면 ( 나올때까지 뺴내는데, 앞쪽에 괄호가 없다면 다 빼내기
        7 5 3 2 * 1 / - +

    [4]
        - * ( -
        7 5 3 2 * 1 / - + 4 4 2

    [5] ) 나오면 ( 나올때까지 뺴내기
        - * (
        7 5 3 2 * 1 / - + 4 4 2 -

    [6] + 보다 / 가 연산순위가 크다 /빼내고 + 넣자 
        - * ( +
        7 5 3 2 * 1 / - + 4 4 2 - 2 / 3

    [5] ) 나오면 ( 나올때까지 뺴내기, 앞쪽에 괄호가 없다면 다 빼내기
        7 5 3 2 * 1 / - + 4 4 2 - 2 / 3 + * -

    [6]
        +
        7 5 3 2 * 1 / - + 4 4 2 - 2 / 3 + * - 3

    [7] 
        7 5 3 2 * 1 / - + 4 4 2 - 2 / 3 + * - 3 +

정답 : 7532*1/-+442-2/3+*-3+

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

for test_case in range(1) :
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
                num.push(op)
            
        # 연산자나 여는 괄호가 나온다면
        else :
            if data == '+' :
                while 1 :
                    if oper.top== -1 or oper.stack[oper.top] == '(' :
                        break
                    op = oper.pop()
                    num.push(op)
            oper.push(data)

    # 남아있는 연산자 빼기
    while oper.top != -1 :
        num.push(oper.pop())