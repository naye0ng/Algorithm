"""
연구소
https://www.acmicpc.net/problem/14502
"""
import collections
import copy

def isNotWall(x,y) :
    global N, M
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True


dx = [-1,0,1,0]
dy = [0,1,0,-1]
def spread() :
    new  = copy.deepcopy(board)
    queue = collections.deque(virus)
    num_virus = len(queue)
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            if isNotWall(x+dx[i], y+dy[i]) and new[x+dx[i]][y+dy[i]] == 0 :
                new[x+dx[i]][y+dy[i]] = 2
                queue.append([x+dx[i],y+dy[i]])
                num_virus += 1
    global N, M, num_wall, result
    result = max(result, N*M-num_wall-num_virus)

def DFS(n) :
    global N, M
    if n == 3 :
        # 퍼트리기
        spread()
    else :
        for x in range(N) :
            for y in range(M) :
                if board[x][y] == 0 :
                    board[x][y] = 1
                    DFS(n+1)
                    board[x][y] = 0
    


N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

virus = []
result, num_wall = 0, 3
for x in range(N) :
    for y in range(M) :
        # 초기 바이러스 부분
        if board[x][y] == 2 :
            virus.append([x,y])
        elif board[x][y] == 1 :
            num_wall += 1
DFS(0)
print(result)