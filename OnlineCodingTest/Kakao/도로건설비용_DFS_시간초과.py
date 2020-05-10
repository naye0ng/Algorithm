# 상0, 오1, 하2, 왼3
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def make_road(x, y, d, cost) :
    global answer
    if cost < answer :
        if x == N-1 and y == N-1 :
            answer = min(answer, cost)
        else :
            for i in range(4) :
                if is_not_wall(x+dx[i],y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                    visited[x+dx[i]][y+dy[i]] = 1
                    if i in [d, (d+2)%4] :
                        # 같은 방향
                        make_road(x+dx[i], y+dy[i], i, cost+100)
                    else :
                        make_road(x+dx[i], y+dy[i], i, cost+600)
                    visited[x+dx[i]][y+dy[i]] = 0

N, answer, visited = 0, 0, 0
def solution(board):
    global answer, N, visited
    N = len(board)
    answer = N*N*600

    visited = board
    visited[0][0] = 1

    # [시간초과] 오른쪽
    if not visited[0][1] :
        visited[0][1] = 1
        make_road(0,1,1,100)
        visited[0][1] = 0
    # 아래쪽
    if not visited[1][0] :
        visited[1][0] = 1
        make_road(1,0,2,100)
        visited[1][0] = 0

    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
# 3800