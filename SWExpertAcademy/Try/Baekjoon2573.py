"""
2573.빙산
"""
class Queue:
    def __init__(self, n):
        self.n = n
        self.front = -1
        self.rear = -1
        self.queue = [None] * self.n

    def inQueue(self, value):
        # # 큐가 포화 상태인 경우 출력
        # if self.isFull() :
        #     print("Full")
        self.near += 1
        self.queue[self.rear] = value

    def deQueue(self):
        # # 큐가 비어있는 경우 출력
        # if self.isEmpty() :
        #     return None
        self.front += 1
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value

    def isEmpty(self):
        return self.front == self.rear

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DownNum(x,y) :
    num = 0
    for i in range(4) :
        if ice[x+dx[i]][y+dy[i]] == 0 :
            num +=1
    return num

def BFS(x,y) :

    temp[x][y] = 0

    # 방문 할 곳이 있다면 체크
    for i in range(4) :
        if temp[x+dx[i]][y+dy[i]]> 0 :
            print("여기에 값있음",temp[x+dx[i]][y+dy[i]])
            #BFS(x+dx[i],y+dy[i])




N, M = map(int,input().split())
ice =[list(map(int, input().split())) for _ in range(N)]
visit = []

print(ice)
# 루트 한번
for x in range(1, N-1) :
    for y in range(1, M-1) :
        if ice[x][y] == 0 :
            continue
        if ice[x][y] == -1 :
            ice[x][y] = 0
            continue
        down = DownNum(x,y)

        ice[x][y] -= down
        if ice[x][y] <= 0 :
            ice[x][y] = -1
        # 다 녹지 않은 빙하라면
        else :
            visit = [x,y]




BFS(visit[0],visit[1])
print("ice",ice)
# 섬찾기
