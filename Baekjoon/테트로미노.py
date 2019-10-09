"""
테트로미노
"""

def isNotWall(x,y) :
    global N, M
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

# 오른쪽 아니면 아래로만 움직이기
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def tetromino(T, path, sumPath) :
    if T == 4 :
        global maxPath
        maxPath = max(maxPath, sumPath)

    else :
        # 모든 path에 대해 갈 수 있는 경로를 모두 검사
        for l in range(len(path)) :
            x, y = path[l]
            for i in range(4) :
                a, b = x+dx[i], y+dy[i]
                if isNotWall(a,b) and visited[a][b] == False :
                    visited[a][b] = True
                    tetromino(T+1, path + [[a,b]], sumPath+board[a][b])
                    visited[a][b] = False



N, M = map(int, input().split())
board = [ list(map(int,input().split())) for _ in range(N)]
visited = [ [0]*M for _ in range(N)]

maxPath = 0
for x in range(N) :
    for y in range(M) :
        visited[x][y] = True
        tetromino(1, [[x,y]], board[x][y])
        visited[x][y] = False

print(maxPath)


"""
오른쪽, 아래쪽만 가도록 만들면 아래 케이스에서 문제가 생길 수 있다.
4 4
0 0 0 0
0 0 0 0
0 0 1 0
0 1 1 1
"""