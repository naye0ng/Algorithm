"""
로봇청소기
https://www.acmicpc.net/problem/4991
"""
# 그때 그때 최적의 경로를 찾는 게 최선이다. 
# 즉, 매 루프마다 visited를 초기화

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def BFS(x, y) :
    visited = [[False]*w for _ in range(h)]
    queue = []
    queue.append([x, y, 0])
    visited[x][y] = True
    while queue :
        x, y, cnt = queue.pop(0)
        for i in range(4) :
            if (0 <= x+dx[i] < h) and ( 0 <= y+dy[i] < w) and visited[x+dx[i]][y+dy[i]] == False :
                if board[x+dx[i]][y+dy[i]] == '*' :
                    # 찾았다 요놈!
                    global dirty, answer
                    dirty -= 1
                    answer += cnt+1
                    board[x+dx[i]][y+dy[i]] = "."
                    return BFS(x+dx[i],y+dy[i])

                elif board[x+dx[i]][y+dy[i]] == '.' :
                    # 계속 움직이기
                    visited[x+dx[i]][y+dy[i]] = True
                    queue.append([x+dx[i],y+dy[i], cnt+1])

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    board = [" ".join(input()).split() for _ in range(h)]

    dirty, answer = 0, 0
    startX, startY = -1, -1
    for x in range(h) :
        for y in range(w) :
            if board[x][y] == 'o' :
                # 다시 지나갈 수 있도록 변경
                board[x][y] = "."
                startX, startY = x, y
            elif board[x][y] == '*' :
                dirty += 1

    BFS(startX, startY)
    if dirty :
        print(-1)
    else :
        print(answer)
