"""
탈출
https://www.acmicpc.net/problem/3055
"""

R, C = map(int,input().split())
board = [" ".join(input()).split() for _ in range(R)]

S = []
water = []
for x in range(R) :
    for y in range(C) :
        if board[x][y] == "S" :
            S.append([x,y])
        elif board[x][y] == "*" :
            water.append([x,y])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 1분 동안
t = 1
is_not_break = True
while is_not_break :
    # [1] 고슴도치 이동
    for _ in range(len(S)) :
        x, y = S.pop(0)
        # 고슴도치가 물에 빠지지 않았으면 계속 이동
        if board[x][y] == "S" :
            for i in range(4) :
                if (x+dx[i] >= 0 and x+dx[i] < R ) and (y+dy[i] >= 0 and y+dy[i] < C) :
                    if  board[x+dx[i]][y+dy[i]] == "." :
                        board[x+dx[i]][y+dy[i]] = "S"
                        S.append([x+dx[i],y+dy[i]])
                    elif board[x+dx[i]][y+dy[i]] == "D" :
                        is_not_break = False
                        break
        if not is_not_break :
            break
    if not is_not_break or not S:
            break
    
    # [2] 물 확장
    for _ in range(len(water)) :
        x, y = water.pop(0)
        for i in range(4) :
            if (x+dx[i] >= 0 and x+dx[i] < R ) and (y+dy[i] >= 0 and y+dy[i] < C) and (board[x+dx[i]][y+dy[i]] == "." or board[x+dx[i]][y+dy[i]] == "S") :
                # 고슴도치는 물에 빠질 수 있음
                board[x+dx[i]][y+dy[i]] = "*" 
                water.append([x+dx[i],y+dy[i]])
    t += 1

if is_not_break :
    print("KAKTUS")
else :
    print(t)