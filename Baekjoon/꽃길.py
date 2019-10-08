"""
꽃길
https://www.acmicpc.net/problem/14620
"""

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 반경 체크
def isOk(x,y) :
    for i in range(4) :
        if visited[x+dx[i]][y+dy[i]] :
            return False
    return True

minTotal = 200000
def seed(n, total):
    if n == 3 :
        global minTotal
        minTotal = min(minTotal, total)
    else :
        for x in range(1, N-1) :
            for y in range(1, N-1) :
                if visited[x][y] == False and isOk(x,y) :
                    visited[x][y] = True
                    T = board[x][y]
                    for i in range(4) :
                        visited[x+dx[i]][y+dy[i]] = True
                        T += board[x+dx[i]][y+dy[i]] 

                    seed(n+1,total+T)

                    visited[x][y] = False
                    for i in range(4) :
                        visited[x+dx[i]][y+dy[i]] = False


N = int(input())
board = [ list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
seed(0,0)
print(minTotal)
