"""
탈주범검거
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
import collections 

def isNotWall(x,y) :
    global N, M
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

T = int(input())
for test_case in range(1, 1+T) :
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    visited[R][C] = True
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = collections.deque([])
    queue.append([R,C,1])
    while queue :
        x, y, t = queue.popleft()
        if t == L :
            break

        if board[x][y] == 1 :
            # 상
            if isNotWall(x+dx[0],y+dy[0]) and visited[x+dx[0]][y+dy[0]] == False and board[x+dx[0]][y+dy[0]] in [1,2,5,6]:
                visited[x+dx[0]][y+dy[0]] = True
                queue.append([x+dx[0], y+dy[0], t+1])
            # 하
            if isNotWall(x+dx[1],y+dy[1]) and visited[x+dx[1]][y+dy[1]] == False and board[x+dx[1]][y+dy[1]] in [1,2,4,7]:
                visited[x+dx[1]][y+dy[1]] = True
                queue.append([x+dx[1], y+dy[1], t+1])
            # 좌
            if isNotWall(x+dx[2],y+dy[2]) and visited[x+dx[2]][y+dy[2]] == False and board[x+dx[2]][y+dy[2]] in [1,3,4,5]:
                visited[x+dx[2]][y+dy[2]] = True
                queue.append([x+dx[2], y+dy[2], t+1])
            # 우
            if isNotWall(x+dx[3],y+dy[3]) and visited[x+dx[3]][y+dy[3]] == False and board[x+dx[3]][y+dy[3]] in [1,3,6,7]:
                visited[x+dx[3]][y+dy[3]] = True
                queue.append([x+dx[3], y+dy[3], t+1])

        elif board[x][y] == 2 :
            # 상
            if isNotWall(x+dx[0],y+dy[0]) and visited[x+dx[0]][y+dy[0]] == False and board[x+dx[0]][y+dy[0]] in [1,2,5,6]:
                visited[x+dx[0]][y+dy[0]] = True
                queue.append([x+dx[0], y+dy[0], t+1])
            # 하
            if isNotWall(x+dx[1],y+dy[1]) and visited[x+dx[1]][y+dy[1]] == False and board[x+dx[1]][y+dy[1]] in [1,2,4,7]:
                visited[x+dx[1]][y+dy[1]] = True
                queue.append([x+dx[1], y+dy[1], t+1])

        elif board[x][y] == 3 :
            # 좌
            if isNotWall(x+dx[2],y+dy[2]) and visited[x+dx[2]][y+dy[2]] == False and board[x+dx[2]][y+dy[2]] in [1,3,4,5]:
                visited[x+dx[2]][y+dy[2]] = True
                queue.append([x+dx[2], y+dy[2], t+1])
            # 우
            if isNotWall(x+dx[3],y+dy[3]) and visited[x+dx[3]][y+dy[3]] == False and board[x+dx[3]][y+dy[3]] in [1,3,6,7]:
                visited[x+dx[3]][y+dy[3]] = True
                queue.append([x+dx[3], y+dy[3], t+1])

        elif board[x][y] == 4 : 
            # 상
            if isNotWall(x+dx[0],y+dy[0]) and visited[x+dx[0]][y+dy[0]] == False and board[x+dx[0]][y+dy[0]] in [1,2,5,6]:
                visited[x+dx[0]][y+dy[0]] = True
                queue.append([x+dx[0], y+dy[0], t+1])
            # 우
            if isNotWall(x+dx[3],y+dy[3]) and visited[x+dx[3]][y+dy[3]] == False and board[x+dx[3]][y+dy[3]] in [1,3,6,7]:
                visited[x+dx[3]][y+dy[3]] = True
                queue.append([x+dx[3], y+dy[3], t+1])

        elif board[x][y] == 5 :
            # 하
            if isNotWall(x+dx[1],y+dy[1]) and visited[x+dx[1]][y+dy[1]] == False and board[x+dx[1]][y+dy[1]] in [1,2,4,7]:
                visited[x+dx[1]][y+dy[1]] = True
                queue.append([x+dx[1], y+dy[1], t+1])
            # 우
            if isNotWall(x+dx[3],y+dy[3]) and visited[x+dx[3]][y+dy[3]] == False and board[x+dx[3]][y+dy[3]] in [1,3,6,7]:
                visited[x+dx[3]][y+dy[3]] = True
                queue.append([x+dx[3], y+dy[3], t+1])

        elif board[x][y] == 6 :
            # 하
            if isNotWall(x+dx[1],y+dy[1]) and visited[x+dx[1]][y+dy[1]] == False and board[x+dx[1]][y+dy[1]] in [1,2,4,7]:
                visited[x+dx[1]][y+dy[1]] = True
                queue.append([x+dx[1], y+dy[1], t+1])
            # 좌
            if isNotWall(x+dx[2],y+dy[2]) and visited[x+dx[2]][y+dy[2]] == False and board[x+dx[2]][y+dy[2]] in [1,3,4,5]:
                visited[x+dx[2]][y+dy[2]] = True
                queue.append([x+dx[2], y+dy[2], t+1])

        elif board[x][y] == 7 :
            # 상
            if isNotWall(x+dx[0],y+dy[0]) and visited[x+dx[0]][y+dy[0]] == False and board[x+dx[0]][y+dy[0]] in [1,2,5,6]:
                visited[x+dx[0]][y+dy[0]] = True
                queue.append([x+dx[0], y+dy[0], t+1])
            # 좌
            if isNotWall(x+dx[2],y+dy[2]) and visited[x+dx[2]][y+dy[2]] == False and board[x+dx[2]][y+dy[2]] in [1,3,4,5]:
                visited[x+dx[2]][y+dy[2]] = True
                queue.append([x+dx[2], y+dy[2], t+1])
    result = 0
    for v in visited :
        result += sum(v)
    print('#{} {}'.format(test_case, result))
    

"""
1
5 6 2 2 6
3 0 0 0 0 3
2 0 0 0 0 6
1 3 1 1 3 1
2 0 2 0 0 2
0 0 4 3 1 1



15
"""