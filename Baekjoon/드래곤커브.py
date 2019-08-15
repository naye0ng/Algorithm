"""
드래곤커브
https://www.acmicpc.net/problem/15685
"""
# dragon direction
gonX = [0, -1, 0, 1]
gonY = [1, 0, -1, 0]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def makeNextCurve(curves,g,G) : 
    if g == G :
        return curves
    i = 0
    nextX, nextY = curves[i][0], curves[i][1]
    nextCurves = []
    while i < len(curves)-1 :
        # 위 => 1
        if curves[i][0] - curves[i+1][0] == 1 :
            nextX += dx[1]
            nextY += dy[1]
        # 아래 => 3
        elif curves[i][0] - curves[i+1][0] == -1 :
            nextX += dx[3]
            nextY += dy[3]
        # 왼쪽 => 0
        elif curves[i][1] - curves[i+1][1] == 1 :
            nextX += dx[0]
            nextY += dy[0]
        # 오른쪽 => 2
        elif curves[i][1] - curves[i+1][1] == -1 :
            nextX += dx[2]
            nextY += dy[2]

        nextCurves.insert(0,[ nextX, nextY])
        i+=1
    return makeNextCurve(nextCurves+curves,g+1,G)
    
# 정사각형 계산
def getSquare(N, dragons) :
    for n in range(N) :
        #  첫번째 계산
        x, y, d = dragons[n][1], dragons[n][0], dragons[n][2]
        nextX, nextY = x+gonX[d], y+gonY[d]
        #  커브 만들기
        curves = [[nextX, nextY],[x,y]]
        finalCurve = makeNextCurve(curves, 0, dragons[n][3])
        i = 0
        while i < len(finalCurve) :
            Board[finalCurve[i][0]][finalCurve[i][1]] = 1
            i +=1 
    # 네모 찾기
    square = 0
    squareX = [0,1,1]
    squareY = [1,1,0]
    # print(Board)
    for x in range(101-1) :
        for y in range(101-1) :
            if Board[x][y] == 1 :
                k = 1
                for i in range(3) :
                    if Board[x+squareX[i]][y+squareY[i]] != 1 :
                        break
                    k += 1
                if k == 4 :
                    square += 1
    return square
            
N = int(input())
dragons = [ list(map(int,input().split())) for _ in range(N)]
Board = [[0]*101 for _ in range(101)]

print(getSquare(N, dragons))