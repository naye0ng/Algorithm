"""
4873.반복문자 지우기
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

T = int(input())
for test_case in range(1, T + 1):
    an = input().replace(""," ").split()

    s = Stack()

    for i in range(len(an)) :
        # 아무것도 없거나 다음 들어올것과 같지 않으면 넣기
        if s.top == -1 or s.stack[s.top] != an[i] :
            s.push(an[i])
        # 이전 값과 같다면 빼기
        elif s.top != -1 and s.stack[s.top] == an[i] :
            s.pop()
    
    print(f'#{test_case} {s.top+1}')

    