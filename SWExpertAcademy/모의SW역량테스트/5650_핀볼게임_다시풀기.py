"""
핀볼게임
"""

def isNotWall(x,y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

# 상(0), 우(1), 하(2), 좌(3)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def moveBall(x,y,d) :
    print("시작2")
    score = 0
    while True :
        # 벽, 블랙홀, 웜홀을 만날때까지 전진
        if isNotWall(x+dx[d],y+dy[d]) :
            # 블랙홀, 본인을 만나는 경우
            if board[x+dx[d]][y+dy[d]] == -1 :
                print("블랙홀")
                return score
            # 이동가능
            elif board[x+dx[d]][y+dy[d]] == 0 :
                print("빈공간")
                x += dx[d]
                y += dy[d]
            # 웜홀
            elif board[x+dx[d]][y+dy[d]] >= 6 :
                print("웜홀")
                score += 1
                if wormhole[board[x+dx[d]][y+dy[d]]][0][0] == x+dx[d] and wormhole[board[x+dx[d]][y+dy[d]]][0][1] == y+dy[d] :
                    x, y = wormhole[board[x+dx[d]][y+dy[d]]][1]
                else :
                    x, y = wormhole[board[x+dx[d]][y+dy[d]]][0]
            # 블록
            elif board[x+dx[d]][y+dy[d]] == 5 :
                print("블록5")
                d = (d+2)%4
            elif board[x+dx[d]][y+dy[d]] == 4 :
                print("블록4")
                if d == 2 :
                    d = 3
                elif d == 1 :
                    d = 0
                else :
                    d = (d + 2) % 4
            elif board[x+dx[d]][y+dy[d]] == 3 :
                print("블록3")
                if d == 1 :
                    d = 2
                elif d == 0 :
                    d = 3
                else :
                    d = (d + 2) % 4
            elif board[x+dx[d]][y+dy[d]] == 2 :
                print("블록2")
                if d == 3 :
                    d = 2
                elif d == 0 :
                    d = 1
                else :
                    d = (d + 2) % 4
            elif board[x+dx[d]][y+dy[d]] == 1 :
                print("블록1")
                if d == 2 :
                    d = 1
                elif d == 3 :
                    d = 0
                else :
                    d = (d + 2) % 4
        else :
            print("벽을 만남")
            d = (d+2)%4


T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]

    # 웜홀 찾기
    wormhole = [[] for _ in range(11)]
    for x in range(N) :
        for y in range(N) :
            if board[x][y] >= 6 :
                wormhole[board[x][y]].append([x,y])

    # 핀볼게임을 블랙홀에서 시작하기?
    maxScore = 0


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