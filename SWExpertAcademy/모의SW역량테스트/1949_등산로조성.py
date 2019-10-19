"""
등산로 조성
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE
"""
def isNotWall(x,y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def makePath(x,y,length,down) :
    global K, minV
    # 사방으로 움직이기
    for i in range(4) :
        # 벽이 아니고 방문한 적 없는 길이면 방문
        if isNotWall(x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] == False :
            # 바로 방문 가능한 경우
            if board[x+dx[i]][y+dy[i]] < board[x][y] :
                visited[x+dx[i]][y+dy[i]] = True
                makePath(x+dx[i],y+dy[i],length+1,down)
                visited[x+dx[i]][y+dy[i]] = False
            # 감소시켜서 방문이 가능한 경우
            if down :
                visited[x+dx[i]][y+dy[i]] = True
                for k in range(K,0,-1) :
                    # k감소한 것이 작아야 함
                    if board[x+dx[i]][y+dy[i]]-k < board[x][y] :
                        board[x+dx[i]][y+dy[i]] -= k
                        makePath(x+dx[i],y+dy[i],length+1, False)
                        board[x+dx[i]][y+dy[i]] += k
                    else :
                        break
                visited[x+dx[i]][y+dy[i]] = False

    minV = max(minV, length)


T = int(input())
for test_case in range(1,1+T) :
    N, K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    # 시작점 찾기
    start, high = [], 0
    for x in range(N) :
        for y in range(N) :
            if board[x][y] > high :
                high = board[x][y]
                start = [[x,y]]
            elif board[x][y] == high :
                start.append([x,y])

    # 시작점을 돌면서 최소값 찾기
    minV = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(len(start)) :
        visited[start[i][0]][start[i][1]] = True
        makePath(start[i][0],start[i][1], 1, True)
        visited[start[i][0]][start[i][1]] = False


    print('#{} {}'.format(test_case, minV))
"""
1
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
"""