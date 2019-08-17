"""
아기상어
https://www.acmicpc.net/workbook/view/1152
"""
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def sharkPath(N, x, y, sharkX, sharkY, size, minPath) :
    # 상어와 먹이의 최소거리 계산
    queue = []
    queue.append([sharkX, sharkY, 0])
    visited = [[False]*N for _ in range(N)]
    while queue :
        shark = queue.pop(0)
        if shark[2] > minPath :
            return 100
        if shark[0] == x and shark[1] == y :
            return shark[2]
        # 상하좌우 다 봐서 갈수 있는 거리의 최소값 찾기
        for i in range(4) :
            if ( shark[0]+dx[i] >= 0 and shark[0]+dx[i] < N ) and (shark[1]+dy[i] >=0 and shark[1]+dy[i] < N) :
                if sea[shark[0]+dx[i]][shark[1]+dy[i]] <= size and visited[shark[0]+dx[i]][shark[1]+dy[i]] == False:
                    visited[shark[0]+dx[i]][shark[1]+dy[i]] = True
                    queue.append([shark[0]+dx[i],shark[1]+dy[i],shark[2]+1])
    return 100


def eatFish(N, sharkX, sharkY, size, eated, total) :
    if eated == size :
        eated = 0
        size += 1
    minPath = 100
    nextX, nextY = 0, 0
    for x in range(N) :
        for y in range(N) :
            # 먹을 수 있는 것들 중 최솟거리 구하기
            if  sea[x][y]!= 0 and sea[x][y] < size :
                path = sharkPath(N, x, y, sharkX, sharkY, size, minPath) 
                if minPath > path :
                    nextX, nextY = x, y
                    minPath = path
    # 잡아먹기
    if minPath != 100 :
        sea[nextX][nextY] = 0
        return eatFish(N, nextX, nextY, size, eated+1, total+minPath)
    return total


N = int(input())
fishes = [0]*7
sea = [ list(map(int,input().split())) for _ in range(N)]
for x in range(N) :
    for y in range(N) :
        if sea[x][y] == 9 :
            sea[x][y] = 0
            print(eatFish(N, x, y, 2, 0, 0))
            break


