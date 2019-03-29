"""
DFS.깊이우선탐색

- input: 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 정점의 갯수가 7이지만 연산을 쉽게하기 위해 양옆, 위 아래로 0을 넣음
# 입력값을 두 개씩 쪼개서 연관배열에 넣기
match = [ [0]*9 for i in range(9)]

inputList =  list(map(int,input().split()))

for i in range(0,len(inputList),2) :
    match[inputList[i]][inputList[i+1]] = 1
    match[inputList[i+1]][inputList[i]] = 1

# 방문체크
check = dict()
for i in range(1,8) :
    check[i] = 0

# 돌아갈곳을 체크할 스택만들기
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

backPoint = Stack()
backPoint.push(1)
check[1] = 1
v = 1
print(1, end='-')
# 지나간 곳 체크
while backPoint.top > -1 :
    for w in range(len(match[v])) :
        # w가 v랑 연관된 곳인데(match==1) 가본적 없으면(check==0) 방문
        if match[v][w] == 1 and check[w] == 0 :
            check[w] = 1
            backPoint.push(w)
            print(w, end='-')
            v = w
            break
        # 남아있는 연관된 곳이 없다면 돌아가기
        if w == len(match[v])-1 :
            v = backPoint.pop()



"""
추가로 각 역할들을 함수로 분리시키자 
"""
