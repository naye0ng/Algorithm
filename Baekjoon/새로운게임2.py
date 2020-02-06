"""
새로운 게임2 
https://www.acmicpc.net/problem/17837
"""
# →, ←, ↑, ↓
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def reverseD(d) :
    if d == 0 :
        return 1
    if d == 1 :
        return 0
    if d == 2 :
        return 3
    if d == 3 :
        return 2

def BlueORWall(x,y) :
    global N 
    if x < 0 or x >= N :
        return True
    if y < 0 or y >= N :
        return True
    if color[x][y] == 2 :
        return True
    return False

def one_loop() :
    global K
    for k in range(K) :
        x, y, d = queue[k]
        is_blue_or_wall = BlueORWall(x+dx[d],y+dy[d])
        # 파란색과 벽 
        if is_blue_or_wall :
            # 방향 반대로 바꿔서 체크
            d = reverseD(d)
            queue[k][2] = d
            if not BlueORWall(x+dx[d],y+dy[d]) :
                # 벽도 아니고 파란색도 아니면? 계속 이동한다고 생각하렴
                is_blue_or_wall = False
            
        # 흰색
        if not is_blue_or_wall and color[x+dx[d]][y+dy[d]] == 0 :
            # 현재 내 위와 아래에 있는 애들
            start = board[x][y].index(k)
            down = board[x][y][:start]
            up = board[x][y][start:]
            
            board[x][y] = down
            board[x+dx[d]][y+dy[d]].extend(up)
            # 쌓이는 것이 4개 이상이면  경우 종료
            if len(board[x+dx[d]][y+dy[d]]) >= 4 :
                return False
            # 자신과 위에 있는 값 위치 변경
            for index in up :
                queue[index][0], queue[index][1] = x+dx[d], y+dy[d]

        # 빨간색
        elif not is_blue_or_wall and color[x+dx[d]][y+dy[d]] == 1 :
            # 현재 내 위와 아래에 있는 애들
            start = board[x][y].index(k)
            down = board[x][y][:start]
            up = board[x][y][start:]
            
            board[x][y] = down
            board[x+dx[d]][y+dy[d]].extend(reversed(up))
            if len(board[x+dx[d]][y+dy[d]]) >= 4 :
                return False

            for index in up :
                queue[index][0], queue[index][1] = x+dx[d], y+dy[d]
    return True


N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]

board = [[[] for i in range(N)] for _ in range(N)]
queue = []
for k in range(K) :
    x, y, d = map(int, input().split())
    queue.append([x-1,y-1,d-1])
    board[x-1][y-1].append(k)

turn = -1
# 1000턴 동안 돌기
for k in range(1,1001) :
    if not one_loop() :
        turn = k
        break

print(turn)