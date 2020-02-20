"""
낚시왕
https://www.acmicpc.net/problem/17143
"""
#위오아왼
di = [0,2,1,3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isWall(x,y) :
    if x < 0 or x >= R :
        return True
    if y < 0 or y >= C :
        return True
    return False

def moveShark() :
    new_board = [[0]*C for _ in range(R)]
    for x in range(R) :
        for y in range(C) :
            if board[x][y] :
                i = board[x][y]
                S, D, Z = shark[i]
                x2, y2 = x, y
                for _ in range(S) :
                    if isWall(x2+dx[D],y2+dy[D]) :
                        # 방향 전환
                        D = (D+2)%4
                        shark[i][1] = D
                    x2 += dx[D]
                    y2 += dy[D]
                if new_board[x2][y2] :
                    # 사이즈가 더 큰 값
                    if shark[new_board[x2][y2]][2] > Z :
                        i = new_board[x2][y2]
                new_board[x2][y2] = i
    return new_board

def fishing(king) :
    for x in range(R) :
        if board[x][king] :
            size = shark[board[x][king]][2]
            board[x][king] = 0
            return size
    return 0

R, C, M = map(int, input().split())
board = [[0]*C for _ in range(R)]

shark = [[] for _ in range(M+1)]
for i in range(1,M+1) :
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1] = i
    shark[i] = [s, di[d-1], z]    # 속력, 이동방향, 크기

size_of_shark = 0
for king in range(C) :
    size_of_shark += fishing(king)
    board = moveShark() 

print(size_of_shark)