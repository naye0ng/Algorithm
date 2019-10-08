"""
뱀
https://www.acmicpc.net/problem/3190
"""
def isWall(x,y) :
    global N 
    if x < 0 or x >= N :
        return True
    if y < 0 or y >= N :
        return True
    return False

N = int(input())
board = [[0]*N for _ in range(N)]

# 사과
for _ in range(int(input())) :
    x, y  = map(int, input().split())
    board[x-1][y-1] = 2

# 뱀
change = []
for _ in range(int(input())) :
    change.append(input().split())

# 시계방향 -> 부터 시작
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 이동
t, i = 1, 0
snake = [[0,0]]
board[0][0] = 1
breakPT = False
while t <= 10000 :
    if change :
        X, C = change.pop(0)
    else :
        X = 10000
    # t초
    while t <= int(X) :
        # 뱀이 머리를 늘려 다음칸으로 이동
        x, y = snake[-1]
        x += dx[i]
        y += dy[i]
        # 자기 몸과 부딪히거나 벽과 만남 정지
        if isWall(x,y) or board[x][y] == 1:
            breakPT = True
            break
        # 사과
        elif board[x][y] == 2 :
            board[x][y] = 1
        else :
            board[x][y] = 1
            # 꼬리 줄이기
            a, b = snake.pop(0)
            board[a][b] = 0
        snake.append([x,y])
        t += 1

    # X초가 끝난 뒤
    if breakPT :
        break
    if C == 'L' :
        i = (i-1)%4
    elif C == 'D' :
        i = (i+1)%4

print(t)