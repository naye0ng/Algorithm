"""
인구이동
https://www.acmicpc.net/problem/16234
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isNotWall(x,y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0  or y >= N :
        return False
    return True

def canUnion(s1,s2) :
    global L, R
    s = abs(s1-s2)
    # 두 나라의 인구 차이가 L명 이상, R명 이하
    if s >= L and s <= R : return True
    return False

def makeUnion() :
    union = [[0]*N for _ in range(N)]
    union_sum = {}  # {연합cnt : [수, 합]}
    cnt = 0  # 연합의 수
    for x in range(N) :
        for y in range(N) :
            if union[x][y] == 0 :
                cnt += 1
                union[x][y] = cnt
                union_sum[cnt] = [1, board[x][y]]
                queue = []
                queue.append([x,y])
                while queue :
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if isNotWall(a+dx[i],b+dy[i]) and not union[a+dx[i]][b+dy[i]] and canUnion(board[a][b],board[a+dx[i]][b+dy[i]]) :
                            union[a+dx[i]][b+dy[i]] = cnt
                            union_sum[cnt][0] += 1
                            union_sum[cnt][1] += board[a+dx[i]][b+dy[i]] 
                            queue.append([a+dx[i],b+dy[i]])

    # 연합이 없는 상태 : 연합 수 == 나라 수
    if cnt == N*N : return True
    
    # 인구 이동
    for x in range(N) :
        for y in range(N) :
            board[x][y] = (union_sum[union[x][y]][1] // union_sum[union[x][y]][0])

    return False


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

T = 0
for t in range(2001) :
    if makeUnion() : 
        T = t
        break
print(T)