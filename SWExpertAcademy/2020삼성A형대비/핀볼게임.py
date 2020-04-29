"""
핀볼게임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo
"""

# 상, 오, 하, 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def pinball_game(x, y, d) :
    start_x, start_y = x, y
    score = 0

    while True :
        # 현재 위치에서 다음 방향 정하기
        is_not_wormhole = True

        # wall
        if not is_not_wall(x,y):
            score += 1
            d = (d+2)%4

        # wormhole
        elif board[x][y] > 10 :
            x, y = wormhole[board[x][y]//10-6][0]
            is_not_wormhole = True
        elif board[x][y] > 5 :
            x, y = wormhole[board[x][y]-6][1]
            is_not_wormhole = True

        # block
        elif board[x][y] == 1 :
            score += 1
            if d == 2 :
                d = 1
            elif d == 3 :
                d = 0
            else :
                d = (d + 2) % 4
        elif board[x][y] == 2 :
            score += 1
            if d == 0 :
                d = 1
            elif d == 3 :
                d = 2
            else :
                d = (d + 2) % 4
        elif board[x][y] == 3 :
            score += 1
            if d == 1:
                d = 2
            elif d == 0:
                d = 3
            else:
                d = (d + 2) % 4
        elif board[x][y] == 4 :
            score += 1
            if d == 2:
                d = 3
            elif d == 1:
                d = 0
            else:
                d = (d + 2) % 4
        elif board[x][y] == 5 :
            score += 1
            d = (d + 2) % 4

        if is_not_wormhole :
            x += dx[d]
            y += dy[d]

        if (x == start_x and y == start_y) or (is_not_wall(x,y) and board[x][y] == -1):
            return score
    return score

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    wormhole = [[] for _ in range(5)]

    for x in range(N) :
        for y in range(N) :
            if board[x][y] > 5 :
                wormhole[board[x][y]-6].append([x,y])
                if len(wormhole[board[x][y]-6]) == 2 :
                    board[x][y] *= 10

    score = 0
    for x in range(N) :
        for y in range(N) :
            if board[x][y] == 0 :
                for d in range(4) :
                    score = max(score,pinball_game(x, y, d))

    print('#{} {}'.format(test_case, score))

"""
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
"""

