"""
주사위돌리기
https://www.acmicpc.net/problem/14499
"""

def isWall(N, M, x, y) :
    if x >= 0 and x < N :
        if y >= 0 and y < M :
            return False
    return True

# 동서북남
dx = [0,0,-1,1]
dy = [1,-1,0,0,]
def moveDice(N, M, x, y) :
    while direction :
        c = direction.pop(0)
        # 범위 조심
        if isWall(N, M, x+dx[c-1], y+dy[c-1]) :
            continue

        # 주사위 굴리기
        # 동쪽 ->
        if c == 1 :
            temp = dice[1][3]
            for i in range(4) :
                dice[1][i], temp = temp, dice[1][i]
        # 서쪽 <-
        if c == 2 :
            temp = dice[1][0]
            for i in range(3,-1,-1) :
                dice[1][i], temp = temp, dice[1][i]
        # 북쪽 
        if c == 3 :
            temp = dice[1][3]
            for i in range(2,-1,-1) :
                dice[i][1], temp = temp, dice[i][1]
            dice[1][3] = temp
        # 남쪽
        if c == 4 :
            temp = dice[1][3]
            for i in range(3) :
                dice[i][1], temp = temp, dice[i][1]
            dice[1][3] = temp
        
        x += dx[c-1]
        y += dy[c-1]
        if board[x][y] == 0 :
            board[x][y] = dice[1][3]
        else :
            dice[1][3], board[x][y] = board[x][y], 0

        print(dice[1][1])
        

N, M, x, y, K = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
direction = list(map(int,input().split()))
dice = [[0]*4 for _ in range(3)]

moveDice(N, M, x, y)