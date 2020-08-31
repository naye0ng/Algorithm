"""
어른상어
https://www.acmicpc.net/problem/19237
"""
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

N, M, K = map(int, input().split())
sharks = [0]*M

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

D = list(map(int, input().split()))
for x in range(N) :
    for y in range(N) :
        if not board[x][y] :
            board[x][y] = []
        else :
            number = board[x][y]-1
            board[x][y] = [number]
            visited[x][y] = K
            sharks[number] = [x, y, D[number]-1]   

directions = [0 for _ in range(M)]
for m in range(M) :
    directions[m] = [list(map(lambda i : int(i)-1, input().split())) for _ in range(4)]

S = M
T = 0
while T < 1000 and S > 1:
    for i in range(M) :
        x, y, d = sharks[i]
        if x == -1 : continue

        is_move = False
        for j in range(4) :
            D = directions[i][d][j%4]
            if is_not_wall(x+dx[D],y+dy[D]) and not visited[x+dx[D]][y+dy[D]]:
                board[x+dx[D]][y+dy[D]].append(i)
                sharks[i] = [x+dx[D],y+dy[D], D]
                is_move = True
                break

        if not is_move :
            for j in range(4) :
                D = directions[i][d][j%4]
                if is_not_wall(x+dx[D],y+dy[D]) and board[x+dx[D]][y+dy[D]][0] == i :
                    sharks[i] = [x+dx[D],y+dy[D], D]
                    is_move = True
                    break

    for x in range(N) :
        for y in range(N) :

            if visited[x][y] : 
                visited[x][y] -= 1
                if visited[x][y] == 0 and board[x][y] :
                    shark = board[x][y][0]
                    if (sharks[shark][0] != x or sharks[shark][1] != y):
                        board[x][y] = []

            if len(board[x][y]) >= 1 :
                board[x][y].sort()
                for i in range(1, len(board[x][y])) :
                    sharks[board[x][y][i]] = [-1,-1,-1]
                    S -= 1
                shark = board[x][y][0]
                if sharks[shark][0] == x and sharks[shark][1] == y :
                    board[x][y] = [board[x][y][0]]
                    visited[x][y] = K
   
    T += 1

if S > 1 :
    print(-1)
else :
    print(T)