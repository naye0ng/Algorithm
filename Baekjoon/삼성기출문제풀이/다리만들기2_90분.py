"""
다리만들기2
https://www.acmicpc.net/problem/17472
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

# 섬만들기
def get_island() :
    I = 2
    for x in range(N) :
        for y in range(M) :
            if board[x][y] == 1 :
                board[x][y] = I
                queue = [[x,y]]
                while queue :
                    """
                    [주의]
                    - 여기서 y값 변경해도 for문이 순차적으로 y를 조작
                    - 그러나 x의 경우...바깥 for문이므로 이후 y에는 영향을 미침
                    """
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if is_not_wall(a+dx[i], b+dy[i]) and board[a+dx[i]][b+dy[i]] == 1 :
                            board[a+dx[i]][b+dy[i]] = I
                            queue.append([a+dx[i], b+dy[i]])
                I += 1
    return I-2

# 섬i에서 섬j로 가는 최소값 찾기, 다리길이는 최소2
def get_bridge() :
    for x in range(N) :
        for y in range(M) :
            if board[x][y] > 1:
                queue = []
                for d in range(4) :
                    if is_not_wall(x+dx[d], y+dy[d]) and board[x+dx[d]][y+dy[d]] == 0:
                        queue.append([x+dx[d], y+dy[d], d, 1])
                while queue :
                    a, b, d, cnt = queue.pop(0)
                    # 같은 방향으로 이동
                    if is_not_wall(a+dx[d], b+dy[d]) :
                        if board[a+dx[d]][b+dy[d]] == 0 :
                            queue.append([a+dx[d], b+dy[d], d, cnt+1])
                        elif board[a+dx[d]][b+dy[d]] != board[x][y] and cnt >= 2 :
                            # 만남
                            if bridge[board[x][y]-2][board[a+dx[d]][b+dy[d]]-2] > cnt :
                                bridge[board[x][y]-2][board[a+dx[d]][b+dy[d]]-2], bridge[board[a+dx[d]][b+dy[d]]-2][board[x][y]-2] = cnt, cnt

def MST() :
    global min_dist
    # 방문한 섬에서 방문하지 않은 섬으로 나가는 값들 중 가장 작은 값
    while True :
        # 다음에 이용한 다리
        dist, J = 100, -1
        for i in range(I) :
            if visited[i] :
                for j in range(I) :
                    if not visited[j] and bridge[i][j] < dist :
                        dist, J = bridge[i][j], j
        if dist == 100 :
            break
        visited[J] = True
        min_dist += dist

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

I = get_island()
bridge = [[100]*I for _ in range(I)]
get_bridge()

visited = [False]*I
X, Y, min_dist = -1, -1, 100
for x in range(I):
    for y in range(I):
        if min_dist > bridge[x][y] :
            X, Y, min_dist = x, y, bridge[x][y]

if min_dist < 100 :
    visited[X], visited[Y] = True, True
    MST()

if sum(visited) == I :
    print(min_dist)
else :
    print(-1)

"""
8 8
0 0 0 0 0 1 0 1
0 1 0 1 0 1 1 0
1 1 1 1 1 1 0 0
0 0 1 0 0 1 0 0
1 1 0 0 0 1 1 0
0 0 0 1 1 1 1 1
0 1 1 0 0 1 1 0
0 0 1 0 1 0 0 1

correct answer: -1
"""