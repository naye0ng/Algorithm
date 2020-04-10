"""
탈주범검거
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
"""
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for test_case in range(1, T+1) :
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    queue = []
    queue.append([R,C])
    """
    탈주범은 처음 위치에 그대로 있을 수도 있다.
    """
    visited = [[False]*M for _ in range(N)]
    visited[R][C] = True
    t = 1
    while t < L :
        for _ in range(len(queue)) :
            x, y = queue.pop(0)
            # 상
            if board[x][y] in [1,2,4,7] :
                if (0 <= x+dx[0] < N ) and (0 <= y+dy[0] < M) and not visited[x+dx[0]][y+dy[0]] and board[x+dx[0]][y+dy[0]] in [1,2,5,6]:
                    visited[x+dx[0]][y+dy[0]] = True
                    queue.append([x+dx[0],y+dy[0]])
            # 하
            if board[x][y] in [1,2,5,6] :
                if (0 <= x+dx[1] < N ) and (0 <= y+dy[1] < M) and not visited[x+dx[1]][y+dy[1]] and board[x+dx[1]][y+dy[1]] in [1,2,4,7]:
                    visited[x+dx[1]][y+dy[1]] = True
                    queue.append([x+dx[1],y+dy[1]])
            # 좌
            if board[x][y] in [1,3,6,7] :
                if (0 <= x+dx[2] < N ) and (0 <= y+dy[2] < M) and not visited[x+dx[2]][y+dy[2]] and board[x+dx[2]][y+dy[2]] in [1,3,4,5]:
                    visited[x+dx[2]][y+dy[2]] = True
                    queue.append([x+dx[2],y+dy[2]])
            # 우
            if board[x][y] in [1,3,4,5] :
                if (0 <= x+dx[3] < N ) and (0 <= y+dy[3] < M) and not visited[x+dx[3]][y+dy[3]] and board[x+dx[3]][y+dy[3]] in [1,3,6,7]:
                    visited[x+dx[3]][y+dy[3]] = True
                    queue.append([x+dx[3],y+dy[3]])        
        t += 1

    result = 0
    for n in range(N) :
        result += sum(visited[n])

    print('#{} {}'.format(test_case, result))