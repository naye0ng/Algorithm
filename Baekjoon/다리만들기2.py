"""
다리 만들기2
https://www.acmicpc.net/problem/17472
"""
import collections

def isNotWall(x,y) :
    global N, M 
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

# 같은 섬 판별하기
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def sameIsland(x,y,k) :
    queue = collections.deque([])
    queue.append([x,y])
    board[x][y] = k
    l = 0
    while l < len(queue) :
        x, y = queue[l]
        for i in range(4) :
            if isNotWall(x+dx[i],y+dy[i]) and board[x+dx[i]][y+dy[i]] == 1 :
                board[x+dx[i]][y+dy[i]] = k
                queue.append([x+dx[i],y+dy[i]])
        l += 1
    island.append(queue)

# i, j의 최소 거리 구하기
def distance(I,J) :
    N, M = len(island[I]), len(island[J])
    d = 11
    for i in range(N) :
        for j in range(M) :
            # x 값이 같다면 검사하는데, 중간에 섬과 걸쳐서는 안됨
            if island[I][i][0] == island[J][j][0] :
                noOpstacle = True
                if island[I][i][1] > island[J][j][1] :
                    # 사이에 있는 y값 검사
                    for y in range(island[J][j][1]+1,island[I][i][1]) :
                        if board[island[I][i][0]][y] != 0 :
                            noOpstacle = False
                            break
                else :
                    # 사이에 있는 y값 검사
                    for y in range(island[I][i][1]+1,island[J][j][1]) :
                        if board[island[I][i][0]][y] != 0 :
                            noOpstacle = False
                            break
                # 사이에 장애물이 없다면 가능
                if noOpstacle :
                    dist = abs(island[I][i][1]-island[J][j][1])-1
                    if dist > 1 :
                        d = min(d,dist) 
            # y 값이 같다면 검사하는데, 중간에 섬과 걸쳐서는 안됨
            elif island[I][i][1] == island[J][j][1] :
                noOpstacle = True
                if island[I][i][0] > island[J][j][0] :
                    # 사이에 있는 x값 검사
                    for x in range(island[J][j][0]+1,island[I][i][0]) :
                        if board[x][island[I][i][1]] != 0 :
                            noOpstacle = False
                            break
                else :
                    for x in range(island[I][i][0]+1,island[J][j][0]) :
                        if board[x][island[I][i][1]] != 0 :
                            noOpstacle = False
                            break
                if noOpstacle :
                    dist = abs(island[I][i][0]-island[J][j][0])-1
                    if dist > 1 :
                        d = min(d,dist) 
    if d == 11 :
        return 0
    return d
 
def isConnect(path) :
    global K
    parent = [i for i in range(K)]
    # path를 두개씩 끊어서 처리
    for i in range(0,len(path),2) :
        # parent[path[i+1]]값을 가진 애들 전부다 바쿼 parent[i]로
        tmp = parent[path[i+1]]
        for j in range(len(parent)) :
            if parent[j] == tmp :
                parent[j] = parent[path[i]]
    # 확인
    t = parent[0]
    for i in range(1,len(parent)) :
        if parent[i] != t :
            return False
    return True

# bridge 조합으로 연결상태 확인, 다리의 개수는 최소 K-1개뽑기
# n : 뽑은 개수, k : 이전에 선택한 값 +1
def combBridge(n,k,length, path) :
    global K, L, result
    if n == K-1 :
        # 연결된거 체크
        if isConnect(path) :
            result = min(result, length)
    else :
        for i in range(k, L) :
            # bridge[i][0], bridge[j][0]을 연결하는 것
            combBridge(n+1,i+1,length+bridge[i][2],path+[bridge[i][0],bridge[i][1]])


  
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
island = []

# 같은 섬 체크
k = 2
for x in range(N) :
    for y in range(M) :
        if board[x][y] == 1 :
            sameIsland(x,y,k)
            k += 1

K = len(island)
bridge = []
for i in range(K-1) :
    for j in range(i+1, K) :
        # i번째 섬이랑 j번쨰 섬 사이의 가장 짧은 거리 찾기
        d = distance(i,j)
        if d > 1:
            bridge.append([i, j, d])

L = len(bridge)

# 연결이 불가능한 경우
result = 100

if len(bridge) >= K-1 :
    combBridge(0,0,0,[])

if result == 100 :
    result = -1

print(result)

"""
3 10
1 1 0 0 0 0 0 0 1 1
1 0 0 0 0 1 0 0 0 1
0 0 1 0 0 0 1 0 1 1
"""
