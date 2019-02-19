"""
4875.미로
"""
class Stack :
    def __init__(self):
        self.top = -1
        self.stack = [0]*1000
    
    def push(self,x,y,w) :
        # 스택에 넣는 순간 벽으로 만들어 버리자
        an[x][y] = 1
        self.top +=1
        self.stack[self.top] = [x,y,w]

    def pop(self) :
        value = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -=1
        # pop하는 순간 다음 꺼 방향 재설정
        if self.top > -1 :
            self.stack[self.top][2] = getnext(self.stack[self.top][0],self.stack[self.top][1])

# 어느방향에 통로가 있는지 반환
def getnext(x,y) :
    # up
    if x-1 >= 0 :
        if an[x-1][y] != 1 :
            return "up"
    # down
    if x+1 < n :
        if an[x+1][y] != 1 :
            return "down"
    # left
    if y-1 >= 0 :
        if an[x][y-1] != 1 :
            return "left"
    # right
    if y+1 < n :
        if an[x][y+1] != 1 :
            return "right"
    # no
    return "no"



T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    an = [list(map(int,input().replace(""," ").split())) for _ in range(n)]

    stack = Stack()
    # 출발점 찾기
    for x in range(n):
        if 2 in an[x] :
            for y in range(n) : 
                # 출발점
                if an[x][y] == 2 :
                    stack.push(x,y,getnext(x,y))
                    break
    result = 0
    while stack.top > -1 :
        x = stack.stack[stack.top][0]
        y = stack.stack[stack.top][1]
        next = stack.stack[stack.top][2]

        # 이동할 방향이 없다면
        if next == "no" :
            stack.pop()
        else :
            # 이동할 방향이 있다면
            if next == "up" :
                if an[x-1][y] == 3 :
                    result = 1
                    break
                stack.push(x-1,y,getnext(x-1,y))
            elif next == "down" :
                if an[x+1][y] == 3 :
                    result = 1
                    break
                stack.push(x+1,y,getnext(x+1,y))
            elif next == "left" :
                if an[x][y-1] == 3 :
                    result = 1
                    break
                stack.push(x,y-1,getnext(x,y-1))
            elif next == "right" :
                if an[x][y+1] == 3 :
                    result = 1
                    break
                stack.push(x,y+1,getnext(x,y+1))

    print(f'#{test_case} {result}')