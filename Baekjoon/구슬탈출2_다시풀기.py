"""
구슬탈출2
"""
# 상(0), 우(1), 하(2), 좌(3)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def moveBlue(x, y, d, x2, y2) :
    global N
    while True :
        if board[x+dx[d]][y+dy[d]] == '.' and not (x+dx[d] == x2 and y+dy[d] == y2) :
            x += dx[d]
            y += dy[d]
        elif board[x+dx[d]][y+dy[d]] == 'O' :
            x += dx[d]
            y += dy[d]
            return  x,y, True
        else :
            return x, y, False

def moveRed(x, y, d, x2, y2) :
    global N
    while True :
        if board[x+dx[d]][y+dy[d]] == '.' and not (x+dx[d] == x2 and y+dy[d] == y2) :
            x += dx[d]
            y += dy[d]
        elif board[x + dx[d]][y + dy[d]] == 'O':
            x += dx[d]
            y += dy[d]
            return x, y, True
        else :
            return x, y, False

# 중력을 이용해서 아래로 기울이기
def Down(n, rx, ry, bx, by) :
    global result
    if n < result - 1:
        redOut, blueOut = False, False
        # 아래로 움직일땐, y값이 같을 때를 주의
        if ry == by :
            # x값이 큰 것 부터 이동
            if rx > bx :
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 2, bx, by)
                # 파란공이동
                bx, by, blueOut= moveBlue(bx, by, 2, rx, ry)
            else :
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 2, rx, ry)
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 2, bx, by)
        else :
            # 순서 상관 없이 이동
            rx, ry, redOut = moveRed(rx, ry, 2, bx, by)
            bx, by, blueOut = moveBlue(bx, by, 2, rx, ry)
        # 모든 이동 후 다시 다른 함수 호출
        if blueOut == False :
            if redOut :
                result = min(result, n+1)
            else :
                # 이동
                Left(n + 1, rx, ry, bx, by)
                Right(n + 1, rx, ry, bx, by)

def UP(n, rx, ry, bx, by) :
    global result
    if n < result - 1:
        redOut, blueOut = False, False
        # 위로 움직일땐, y값이 같을 때를 주의
        if ry == by:
            # x값이 작은 것 부터 이동
            if rx > bx:
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 0, rx, ry)
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 0, bx, by)
            else:
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 0, bx, by)
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 0, rx, ry)
        else:
            # 순서 상관 없이 이동
            rx, ry, redOut = moveRed(rx, ry, 0, bx, by)
            bx, by, blueOut = moveBlue(bx, by, 0, rx, ry)
        # 모든 이동 후 다시 다른 함수 호출
        if blueOut == False:
            if redOut:
                result = min(result, n+1)
            else:
                # 이동
                Left(n+1, rx, ry, bx, by)
                Right(n+1, rx, ry, bx, by)

def Left(n, rx, ry, bx, by) :
    global result
    if n < result - 1:
        redOut, blueOut = False, False
        # 왼쪽으로 움직일땐, x값이 같을 때를 주의
        if rx == bx:
            # y값이 작은 것 부터 이동
            if ry > by:
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 3, rx, ry)
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 3, bx, by)
            else:
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 3, bx, by)
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 3, rx, ry)
        else:
            # 순서 상관 없이 이동
            rx, ry, redOut = moveRed(rx, ry, 3, bx, by)
            bx, by, blueOut = moveBlue(bx, by, 3, rx, ry)
        # 모든 이동 후 다시 다른 함수 호출
        if blueOut == False:
            if redOut:
                result = min(result, n+1)
            else:
                Down(n+1,rx, ry, bx, by)
                UP(n+1,rx, ry, bx, by)

def Right(n, rx, ry, bx, by) :
    global result
    if n < result - 1:
        redOut, blueOut = False, False
        # 오른쪽으로 움직일땐, x값이 같을 때를 주의
        if rx == bx:
            # y값이 큰은 것 부터 이동
            if ry > by:
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 1, bx, by)
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 1, rx, ry)
            else:
                # 파란공이동
                bx, by, blueOut = moveBlue(bx, by, 1, rx, ry)
                # 빨간공 이동
                rx, ry, redOut = moveRed(rx, ry, 1, bx, by)
        else:
            # 순서 상관 없이 이동
            rx, ry, redOut = moveRed(rx, ry, 1, bx, by)
            bx, by, blueOut = moveBlue(bx, by, 1, rx, ry)
        # 모든 이동 후 다시 다른 함수 호출
        if blueOut == False:
            if redOut:
                result = min(result, n+1)
            else:
                Down(n+1,rx, ry, bx, by)
                UP(n+1,rx, ry, bx, by)


N, M = map(int,input().split())
board = [" ".join(input()).split() for _ in range(N)]

result = 11

# 빨간공, 파란공 위치 찾기
rx, ry, bx, by = 0, 0, 0, 0
for x in range(N) :
    for y in range(M) :
        if board[x][y] == 'R' :
            rx, ry = x, y
            board[x][y] = '.'
        elif board[x][y] == 'B' :
            bx, by = x, y
            board[x][y] = '.'

Left(0, rx, ry, bx, by)
Right(0, rx, ry, bx, by)
Down(0,rx, ry, bx, by)
UP(0,rx, ry, bx, by)

if result == 11 :
    result = -1
print(result)
"""
7 7
#######
#....B#
#.#####
#....R#
#####.#
#O....#
#######
"""