"""
2105 - 디저트 카페
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE
"""
def isWall(x,y) :
    global N
    if x < 0 or x >= N :
        return True
    if y < 0 or y >= N :
        return True
    return False

dx = [-1,1,1,-1]
dy = [1,1,-1,-1]
def eatDessert(N) :
    maxPath = -1
    for X in range(1,N-1) :
        for Y in range(N-2) :
            for a in range(N,0,-1) :
                for b in range(N,0,-1) :
                    # [개선 방안] 꼭지점을 최상단으로 잡았으면, isWall(X+a,Y+b)만 해도 됨 >> x,y가 증가하는 방향으로 움직이므로!
                    # 벽이 아니면서, 최대값이라면?
                    if isWall(X+dx[0]*a,Y+dy[0]*a) == False and isWall(X+dx[0]*a+dx[1]*b,Y+dy[0]*a+dx[1]*b) == False and (a+b)*2 > maxPath :
                        # print(a,b)
                        x,y = X, Y
                        # 다먹을 수 있는지 체크
                        dessert = [False]*101
                        isBreak = False
                        # [1] 0번 방향
                        for _ in range(a) :
                            x += dx[0]
                            y += dy[0]
                            if isWall(x,y) or dessert[board[x][y]] :
                                isBreak = True
                                break
                            dessert[board[x][y]] = True
                        if isBreak :
                            continue
                        # [2] 1번 방향
                        for _ in range(b) :
                            x += dx[1]
                            y += dy[1]
                            if isWall(x,y) or dessert[board[x][y]] :
                                isBreak = True
                                break
                            dessert[board[x][y]] = True
                        if isBreak :
                            continue
                        # [3] 2번 방향
                        for _ in range(a) :
                            x += dx[2]
                            y += dy[2]
                            if isWall(x,y) or dessert[board[x][y]] :
                                isBreak = True
                                break
                            dessert[board[x][y]] = True
                        if isBreak :
                            continue
                        # [4] 3번 방향
                        for _ in range(b) :
                            x += dx[3]
                            y += dy[3]
                            if isWall(x,y) or dessert[board[x][y]] :
                                isBreak = True
                                break
                            dessert[board[x][y]] = True
                        if isBreak :
                            continue
                        maxPath = (a+b)*2
    return maxPath

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    print("#{} {}".format(test_case, eatDessert(N)))
"""
1
7
7 4 1 5 1 7 9
9 4 6 1 4 6 8
9 6 4 8 4 7 4
3 2 6 2 4 2 8
4 9 4 6 2 4 7
1 7 6 8 9 5 8
1 9 4 7 2 9 7



1         
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
"""