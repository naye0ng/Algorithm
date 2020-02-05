"""
미세먼지안녕
https://www.acmicpc.net/problem/17144
"""
# 시계방향 : 오,아,왼,위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def isNotWall(x,y) :
    global R, C
    if x < 0 or x >= R :
        return False
    if y < 0 or y >= C :
        return False
    return True

def dust(R,C) :
    next_board = [[0]*C for _ in range(R)]
    for x in range(R) :
        for y in range(C) :
            if board[x][y] == -1 :
                next_board[x][y] = -1
            elif board[x][y] > 0 :
                # 미세먼지 확산 : 공기청정기만 아니면 무조건 확산(미세먼지 있어도 확산)
                cnt = 0
                for i in range(4) :
                    if isNotWall(x+dx[i],y+dy[i]) and board[x+dx[i]][y+dy[i]] != -1 :
                        cnt += 1
                        next_board[x+dx[i]][y+dy[i]] += board[x][y]//5
                next_board[x][y] += board[x][y] - (board[x][y]//5)*cnt
    return next_board

def airclear(R,C) :
    x1, x2 = 0, 0
    for x in range(2,R-2) :
        if board[x][0] == -1 :
            x1, x2 = x, x+1
            break

    # [1] 오른쪽으로 C만큼
    tmp1, tmp2 = 0, 0
    for y in range(1,C) :
        tmp1, board[x1][y] = board[x1][y], tmp1
        tmp2, board[x2][y] = board[x2][y], tmp2
    

    # [2-1] 위쪽으로 이동
    for x in range(x1-1,-1,-1) :
        tmp1, board[x][y] = board[x][y], tmp1
    # [2-2] 아래쪽으로 이동
    for x in range(x2+1,R) :
        tmp2, board[x][y] = board[x][y], tmp2
    
    # [3] 왼쪽으로 이동 
    for y in range(C-2,-1,-1) :
        tmp1, board[0][y] = board[0][y], tmp1
        tmp2, board[R-1][y] = board[R-1][y], tmp2
    
    # [4-1] 아래로 이동
    for x in range(1,x1) :
        tmp1, board[x][y] = board[x][y], tmp1
    # [4-2] 위로 이동
    for x in range(R-2,x2,-1) :
        tmp2, board[x][y] = board[x][y], tmp2

R, C, T = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(R) ]

for t in range(T) :
    # 확산
    board = dust(R,C)
    # 공기청정기 작동
    airclear(R,C)

result = 0
for x in range(R) :
    for y in range(C) :
        if board[x][y] > 0 : result += board[x][y]

print(result)