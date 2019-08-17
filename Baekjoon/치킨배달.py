"""
치킨배달
https://www.acmicpc.net/problem/15686
"""
minPath = 2500
def getMinPath(H) :
    global minPath
    total = 0
    for h in range(H) :
        total += min(home_to_chicken[h])
    minPath = min(total,minPath)
    
# 조합만들기 : n을 사용한 중복 제거
def selectChicken(C, H, M, depth, n) :
    if depth == M :
        for i in range(C) :
            if visited[i] == False :
                for h in range(H) :
                    home_to_chicken[h][i] = home_to_chicken[h][i]*10000
        getMinPath(H)
        for i in range(C) :
            if visited[i] == False :
                for h in range(H) :
                    home_to_chicken[h][i] = home_to_chicken[h][i]//10000
    else :
        for i in range(n, C) :
            if visited[i] == False :
                visited[i] = True
                selectChicken(C, H, M, depth+1, i)
                visited[i] = False 

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []
for x in range(N) :
    for y in range(N) :
        if city[x][y] == 1 :
            home.append([x,y])
        elif city[x][y] == 2 :
            chicken.append([x,y])
C = len(chicken)
H = len(home)

#[시간초과 해결방법] 치킨집과 집의 위치는 변하지 않는다 >> 죽, 치킨집과 집 사이의 거리를 미리 구해두는 것!
home_to_chicken = [[0]*C for _ in range(H)]
for h in range(H) :
    for c in range(C) :
        home_to_chicken[h][c] = abs(home[h][0]-chicken[c][0]) + abs(home[h][1]-chicken[c][1])
visited = [False]*C
selectChicken(C, H, M, 0, 0)
print(minPath)