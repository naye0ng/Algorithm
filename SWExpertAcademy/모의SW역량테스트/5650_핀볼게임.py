"""
5650 - 핀볼게임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&categoryId=AWXRF8s6ezEDFAUo&categoryType=CODE
"""

def isWall(x,y) :
    global N
    if x >= 0 and x < N :
        if y >= 0 and y < N :
            return False
    return True

# 상0 오1 하2 왼3
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def oneLoop(startX, startY, x, y, d) :
    score = 0
    while True :
        if isWall(x,y) :
            x += dx[(d+2)%4]
            y += dy[(d+2)%4]
            d = (d+2)%4
            score += 1
        elif board[x][y] == -1 or (startX == x and startY == y) :
            break
        # 웜홀
        elif board[x][y] >= 6 :
            for i in range(2) :
                if w_holes[board[x][y]][i][0] != x or w_holes[board[x][y]][i][1] != y :
                    x, y = w_holes[board[x][y]][i][0]+dx[d], w_holes[board[x][y]][i][1]+dy[d]
                    break
        elif board[x][y] == 1 :
            if d == 2 :
                d = 1
                x += dx[d]
                y += dy[d]
                score += 1 
            elif d == 3 :
                d = 0
                x += dx[d]
                y += dy[d]
                score += 1 
            else :
                d = (d+2)%4
                x += dx[d]
                y += dy[d]
                score += 1 
        elif board[x][y] == 2 :
            if d == 3 :
                d = 2
                x += dx[d]
                y += dy[d]
                score += 1
            elif d == 0 :
                d = 1
                x += dx[d]
                y += dy[d]
                score += 1
            else :
                d = (d+2)%4
                x += dx[d]
                y += dy[d]
                score += 1 
        elif board[x][y] == 3 :
            if d == 1 :
                d = 2
                x += dx[d]
                y += dy[d]
                score += 1
            elif d == 0 :
                d = 3
                x += dx[d]
                y += dy[d]
                score += 1
            else :
                d = (d+2)%4
                x += dx[d]
                y += dy[d]
                score += 1 
        elif board[x][y] == 4 :
            if d == 2 :
                d = 3
                x += dx[d]
                y += dy[d]
                score += 1
            elif d == 1 :
                d = 0
                x += dx[d]
                y += dy[d]
                score += 1
            else :
                d = (d+2)%4
                x += dx[d]
                y += dy[d]
                score += 1 
        elif board[x][y] == 5 :
            d = (d+2)%4
            x += dx[d]
            y += dy[d]
            score += 1 
        else :
            x += dx[d]
            y += dy[d]
    return score

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    w_holes = [[] for _ in range(11)]
    # 웜홀 
    for x in range(N) :
        for y in range(N) :
            if board[x][y] >= 6 :
                w_holes[board[x][y]].append([x,y])
    score = 0
    for x in range(N) :
        for y in range(N) :
            for d in range(4) :
                if board[x][y] == 0 :
                    score = max(score,oneLoop(x, y, x+dx[d], y+dy[d], d))
    print('#{} {}'.format(test_case,score))