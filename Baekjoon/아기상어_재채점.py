"""
아기상어
https://www.acmicpc.net/problem/16236
"""

def isNotWall(x, y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0  or y >= N :
        return False
    return True

# 위, 왼, 오, 아
dx = [-1,0,0,1]
dy = [0,-1,1,0] 
def eatFish(N,x,y) :
    size, eaten, T = 2, 0, 0
    queue = [[T, x,y]]
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    isSort = False
    while queue :
        t, x, y = queue.pop(0)
        # 동일한 시간대의 값 들 중 가장 위쪽을 확인하기 위함
        if queue and queue[0][0] != t :
            isSort = True
        # 현재 위치에 먹을 것이 없다면, 이동
        if board[x][y] in [size, 0] :
            for i in range(4) :
                if isNotWall(x+dx[i],y+dy[i]) and visited[x+dx[i]][y+dy[i]] == False :
                    # 이동할 수 있다면, 이동
                    if board[x+dx[i]][y+dy[i]] <= size :
                        visited[x+dx[i]][y+dy[i]] = True
                        queue.append([t+1, x+dx[i], y+dy[i]])
            if isSort :
                isSort = False
                queue.sort()
        # 먹을 것이 있다면 먹음, 현재 위치에서 새로 시작
        else :
            board[x][y] = 0
            visited = [[False]*N for _ in range(N)]
            visited[x][y] = 0
            T = t
            queue = [[T, x, y]]
            eaten += 1
            if eaten == size :
                size += 1
                eaten = 0
    return T

N = int(input())
board = [ list(map(int, input().split())) for _ in range(N) ] 

fish = [[] for _ in range(6)]
x, y = 0, 0
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 9 :
            x, y  = i, j
        elif board[i][j] != 0 :
            fish[board[i][j]-1].append([i, j])
board[x][y] = 0
print(eatFish(N,x,y))
