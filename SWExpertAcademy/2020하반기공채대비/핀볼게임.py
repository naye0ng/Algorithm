'''
핀볼게임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&categoryId=AWXRF8s6ezEDFAUo&categoryType=CODE
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x, y) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= N : return False
    return True

def get_score(X, Y, d) :
    score = 0
    x = X + dx[d]
    y = Y + dy[d]
    while True :
        if x == X and y == Y : return score
        if board[x][y] == -1 : return score

        # 웜홀
        if board[x][y] >= 6 : 
            wx, wy = wormhole[board[x][y]-6][0]
            if wx == x and wy == y :
                x, y = wormhole[board[x][y]-6][1]
            else :
                x, y = wx, wy

        # 블록
        if board[x][y] == 1 : 
            score += 1
            if d == 2 :
                d = 1
            elif d == 3 : 
                d = 0
            else :
                d = (d+2)%4
        elif board[x][y] == 2 :
            score += 1 
            if d == 3 :
                d = 2
            elif d == 0 : 
                d = 1
            else :
                d = (d+2)%4
        elif board[x][y] == 3 : 
            score += 1
            if d == 1 :
                d = 2
            elif d == 0 : 
                d = 3
            else :
                d = (d+2)%4
        elif board[x][y] == 4 : 
            score += 1
            if d == 1 :
                d = 0
            elif d == 2 : 
                d = 3
            else :
                d = (d+2)%4
        elif board[x][y] == 5 :
            score += 1
            d = (d+2)%4
        
        if not is_not_wall(x+dx[d],y+dy[d]):
            score += 1
            d = (d+2)%4
            continue

        x += dx[d]
        y += dy[d]

    return score


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    wormhole = [[] for _ in range(5)]
    for x in range(N) :
        for y in range(N) :
            if board[x][y] < 6 : continue
            wormhole[board[x][y]-6].append([x, y])
    
    max_score = 0
    for x in range(N) :
        for y in range(N) :
            if board[x][y] != 0 : continue
            for i in range(4) :
                if is_not_wall(x+dx[i], y+dy[i]) :
                    max_score = max(max_score, get_score(x, y, i))


    print('#{} {}'.format(test_case, max_score))