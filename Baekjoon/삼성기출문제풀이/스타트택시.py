"""
스타트 택시
https://www.acmicpc.net/problem/19238
"""
def convert_wall(i) :
    if i == 1 : return -1
    return i

def is_not_wall(x, y) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= N : return False
    return True

N, M, F = map(int, input().split())
board = [list(map(lambda i : convert_wall(int(i)), input().split())) for _ in range(N)]
x, y = map(lambda i : int(i)-1, input().split())
P = [[] for _ in range(M+1)]
for n in range(1, M+1) :
    x1, y1, x2, y2 = map(lambda i : int(i)-1, input().split())
    P[n] = [x1, y1, x2, y2]
    board[x1][y1] = n

dx = [-1,0,0,1]
dy = [0,-1,1,0]
not_arrived = M
while F and not_arrived:
    queue = [[x, y, 0]]
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    passenger = False
    while queue :
        queue.sort()
        for _ in range(len(queue)) :
            x, y, t = queue.pop(0)
            if board[x][y] > 0 : 
                F -= t
                queue = []
                passenger = True
                break
            else : 
                for i in range(4) :
                    if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] and board[x+dx[i]][y+dy[i]] != -1 :
                        queue.append([x+dx[i], y+dy[i], t+1])
                        visited[x+dx[i]][y+dy[i]] = 1

    if F <= 0 or not passenger:
        break

    number = board[x][y]
    queue = [[x, y, 0]]
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    board[x][y] = 0
    x2, y2 = P[number][2], P[number][3]
    while queue :
        x, y, t = queue.pop(0)
        if x == x2 and y == y2 :
            F -= t
            if F >= 0 :
                F += t*2
                not_arrived -= 1
            break
        else :
            for i in range(4) :
                if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] and board[x+dx[i]][y+dy[i]] != -1 :
                    queue.append([x+dx[i], y+dy[i], t+1])
                    visited[x+dx[i]][y+dy[i]] = 1

if not_arrived :
    print(-1)
else :
    print(F)
