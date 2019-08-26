"""
배열돌리기3
https://www.acmicpc.net/problem/16935
"""

# 상하반전
def move01(N, M, arr) :
    for x in range(N//2) :
        arr[x], arr[(N-1)-x] = arr[(N-1)-x], arr[x]
    return arr

# 좌우반전
def move02(N, M, arr) :
    for y in range(M//2) :
        for x in range(N) :
            arr[x][y], arr[x][M-1-y] = arr[x][M-1-y], arr[x][y]
    return arr

# 오른쪽 90도 회전
def move03(N,M,arr) :
    temp = [[0]*N for _ in range(M)]
    for x in range(N) :
        for y in range(M) :
            temp[y][N-1-x] = arr[x][y]
    return temp

# 왼쪽 90도 회전
def move04(N,M,arr) :
    temp = [[0]*N for _ in range(M)]
    for x in range(N) :
        for y in range(M) :
            temp[M-1-y][x] = arr[x][y]

    return temp

# 배열 돌리기
def move05(N,M,arr) :
    temp = [[0]*M for _ in range(N)]
    # 1
    for x in range(N//2) :
        for y in range(M//2) :
            temp[x][(M//2)+y] = arr[x][y]     
    # 2
    for x in range(N//2) :
        for y in range(M//2, M) :
            temp[N//2+x][y] = arr[x][y]
    # 3
    for x in range(N//2, N) :
        for y in range(M//2, M) :
            temp[x][y-(M//2)] = arr[x][y]
    # 4
    for x in range(N//2, N) :
        for y in range(M//2) :
            temp[x-(N//2)][y] = arr[x][y]
    return temp
# 배열 돌리기
def move06(N,M,arr) :
    temp = [[0]*M for _ in range(N)]
    # 1
    for x in range(N//2) :
        for y in range(M//2) :
            temp[x+N//2][y] = arr[x][y]     
    # 2
    for x in range(N//2) :
        for y in range(M//2, M) :
            temp[x][y-(M//2)] = arr[x][y]
    # 3
    for x in range(N//2, N) :
        for y in range(M//2, M) :
            temp[x-(N//2)][y] = arr[x][y]
    # 4
    for x in range(N//2, N) :
        for y in range(M//2) :
            temp[x][y+(M//2)] = arr[x][y]
    return temp

def doOper(N,M,arr) :
    while queue :
        q = queue.pop(0)
        if q == 1 :
            arr = move01(N,M,arr)
        elif q == 2 :
            arr = move02(N,M,arr)
        elif q == 3 :
            arr = move03(N,M,arr)
        elif q == 4 :
            arr = move04(N,M,arr)
        elif q == 5 :
            arr = move05(N,M,arr)
        elif q == 6 :
            arr = move06(N,M,arr)
        N, M = len(arr), len(arr[0])
    for x in range(len(arr)) :
        print(" ".join(arr[x]))

N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]
queue = list(map(int, input().split()))
doOper(N,M,arr)