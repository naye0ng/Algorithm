# 상0, 오1, 하2, 왼3
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(N, x, y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def solution(board):
    N = len(board)
    visited = [[N*N*600]*N for _ in range(N)]

    answer = N*N*600
    queue = []
    visited[0][0] = 0
    if not board[0][1] :
        # 오른쪽
        visited[0][1] = 100
        queue.append([0,1,1,100])
    if not board[1][0] :
        # 아래쪽
        visited[1][0] = 100
        queue.append([1,0,2,100])

    while queue :
        for _ in range(len(queue)) :
            x, y, d, cost = queue.pop(0)
            for i in range(4) :
                if i == (d+2)%4 :
                    continue
                # 현재 cost보다 크다면 확힌한다.
                if is_not_wall(N, x+dx[i], y+dy[i]) and not board[x+dx[i]][y+dy[i]] and visited[x+dx[i]][y+dy[i]] > cost :
                    if i == d and visited[x+dx[i]][y+dy[i]] >= cost+100 :
                        visited[x+dx[i]][y+dy[i]] = cost+100
                        queue.append([x+dx[i], y+dy[i], i, cost+100])
                    elif i != d and visited[x+dx[i]][y+dy[i]] >= cost+600 :
                        visited[x+dx[i]][y+dy[i]] = cost+600
                        queue.append([x+dx[i], y+dy[i], i, cost+600])

    return visited[N-1][N-1]

print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
