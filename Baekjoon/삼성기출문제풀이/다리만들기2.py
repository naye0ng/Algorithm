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

# MST : 가장 낮은 가중치를 매번 선택하여, n-1개의 간선 찾기
def connect_island(n, L) :
    if n == I-1 :
        global minL
        minL = min(minL, L)
    else :
        B1, B2, minB = -1, -1, 11
        for x in range(I):
            # 현재 이어진 섬들과
            if visited_island[x] :
                for y in range(I):
                    # 다음에 이어질 섬 체크
                    if not visited_island[y] and bridge[x][y] and bridge[x][y] < minB:
                            B1, B2, minB = x, y, bridge[x][y]
        if minB != 11 :
            visited_island[B2] = True
            connect_island(n+1, L+minB)

N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

# 같은 섬 체크
I = 2
for x in range(N) :
    for y in range(M) :
        if board[x][y] == 1 :
            board[x][y] = I
            queue = [[x,y]]
            while queue :
                a,b = queue.pop(0)
                for i in range(4) :
                    if is_not_wall(a+dx[i], b+dy[i]) and board[a+dx[i]][b+dy[i]] == 1 :
                        board[a + dx[i]][b + dy[i]] = I
                        queue.append([a+dx[i], b+dy[i]])
            I += 1
I-=2
# 다리 만들기
bridge = [[0]*I for _ in range(I)]
for x in range(N) :
    for y in range(M) :
        if board[x][y] :
            make_bridge = []
            for i in range(4) :
                if is_not_wall(x+dx[i], y+dy[i]) and board[x+dx[i]][y+dy[i]] == 0 :
                    make_bridge.append([x+dx[i], y+dy[i], i, 1])

            while make_bridge :
                a, b, i, l = make_bridge.pop(0)

                # 같은 방향으로 고!
                if is_not_wall(a+dx[i],b+dy[i]) :
                    if board[a+dx[i]][b+dy[i]] == 0 :
                        make_bridge.append([a+dx[i], b+dy[i], i, l+1])
                    elif l >= 2 and board[x][y] != board[a+dx[i]][b+dy[i]]:
                        """
                        [반례2]에서 같은 섬에서 같은 섬으로 이어지는 다리가 생기므로, 다른 다리임을 체크해준다!
                        """
                        if bridge[board[x][y]-2][board[a+dx[i]][b+dy[i]]-2] == 0 or bridge[board[x][y]-2][board[a+dx[i]][b+dy[i]]-2] > l :
                            bridge[board[x][y]-2][board[a+dx[i]][b+dy[i]]-2], bridge[board[a+dx[i]][b+dy[i]]-2][board[x][y]-2] = l, l

# MST 시작값 찾기
B1, B2, minB = 0, 0, 11
for x in range(I) :
    for y in range(I) :
        if bridge[x][y] :
            if bridge[x][y] and bridge[x][y] < minB :
                B1, B2, minB = x, y, bridge[x][y]

minL = N*M
if minB != 11 :
    visited_island = [False]*I
    visited_island[B1], visited_island[B2] = True, True
    connect_island(1, minB)

if minL == N*M :
    minL = -1
print(minL)

"""
10 10
0 0 0 1 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 1
0 0 0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
1 0 0 1 0 0 0 0 0 1
0 0 0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
0 0 1 1 1 1 0 0 1 1
답 : 11

10 8
0 0 1 1 1 1 1 0
1 1 1 1 1 1 0 1
0 0 0 1 0 1 0 0
1 1 0 1 1 0 1 1
0 0 1 1 0 1 1 0
0 1 0 0 0 0 0 0
1 1 1 1 0 0 1 0
1 0 0 1 1 1 0 0
1 1 0 0 0 1 1 1
1 1 1 0 0 1 0 1
답 : -1
"""