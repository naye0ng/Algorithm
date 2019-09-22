def isWall(N,M,x,y) :
    if x < 0 or x >= N : return True
    elif y < 0 or y >= M : return True
    return False

N, M = map(int, input().strip().split(' '))
cX, cY = map(int, input().strip().split(' '))
board = [[0]*M for _ in range(N)]
board[cX][cY] = 1

# 코니를 잡을 수 없는 경우는 코니가 공간 밖일 때
if isWall(N,M,cX,cY) :
    print('fail')
else :
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    T = 100000
    V = 0
    queue = [[0,0,0]]
    while queue :
        x, y, t = queue.pop(0)
        if T >= t and x == cX and y == cY :
            T = t
            V += 1
        elif T < t and x == cX and y == cY :
            break
        for i in range(4) :
            if isWall(N,M,x+dx[i],y+dy[i]) == False  :
                queue.append([x+dx[i],y+dy[i],t+1])  
    print(T)
    print(V)
