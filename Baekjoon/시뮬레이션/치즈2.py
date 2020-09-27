'''
치즈
https://www.acmicpc.net/problem/2638
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x, y) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= M : return False
    return True

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

queue = [[0,0]]
board[0][0] = -1
while queue :
    x, y = queue.pop(0)
    for i in range(4) :
        if is_not_wall(x+dx[i], y+dy[i]) and board[x+dx[i]][y+dy[i]] == 0 :
            queue.append([x+dx[i], y+dy[i]])
            board[x+dx[i]][y+dy[i]] = -1

queue = []
for x in range(1, N-1) :
    for y in range(1, M-1) :
        if board[x][y] != 1 : continue
        queue.append([x, y])

t = 0
while queue :
    next_air = []
    for _ in range(len(queue)) :
        x, y = queue.pop(0)
        air = 0
        for i in range(4) :
            if is_not_wall(x+dx[i], y+dy[i]) and board[x+dx[i]][y+dy[i]] == -1 :
                air += 1

        if air >= 2 :
            board[x][y] = 0
            next_air.append([x,y])
            # continue
        else :
            queue.append([x,y])

    while next_air :
        x, y = next_air.pop(0)
        board[x][y] = -1
        for i in range(4) :
            if is_not_wall(x+dx[i], y+dy[i]) and board[x+dx[i]][y+dy[i]] == 0 :
                board[x+dx[i]][y+dy[i]] = -1
                next_air.append([x+dx[i], y+dy[i]])

    t += 1
print(t)