'''
치즈
https://www.acmicpc.net/problem/2636
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x, y) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= M : return False
    return True
   
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

t = 0
lenth_of_cheese = 0
while True:
    visited = [[-1]*M for _ in range(N)]
    x, y = 0, 0
    visited[x][y] = t
    queue = [[x,y]]
    cheese = 0
    while queue :
        x, y = queue.pop(0)
        for i in range(4) :
            if is_not_wall(x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] == -1 :
                if board[x+dx[i]][y+dy[i]] == 0 :
                    queue.append([x+dx[i], y+dy[i]])
                    visited[x+dx[i]][y+dy[i]] = t
                else :
                    cheese += 1
                    visited[x+dx[i]][y+dy[i]] = t+1
                    board[x+dx[i]][y+dy[i]] = 0

    if not cheese : break
    lenth_of_cheese = cheese
    t += 1

print(t)
print(lenth_of_cheese)