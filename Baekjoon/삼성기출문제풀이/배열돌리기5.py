"""
배열돌리기5
https://www.acmicpc.net/problem/17470
"""
def up_and_down() :
    for x in range(N//2) :
        for y in range(M) :
            A[x][y], A[N-1-x][y] = A[N-1-x][y], A[x][y]

def left_and_right() :
    for y in range(M//2) :
        for x in range(N) :
            A[x][y], A[x][M-1-y] = A[x][M-1-y], A[x][y]

def rotate_right_90() :
    global A, N, M
    A2 = [[0] * N for _ in range(M)]
    for x in range(N) :
        for y in range(M) :
            A2[y][N-1-x] = A[x][y]
    A, N, M = A2, M, N

def rotate_left_90() :
    global A, N, M
    A2 = [[0]*N for _ in range(M)]
    for x in range(N) :
        for y in range(M) :
            A2[M-1-y][x] = A[x][y]
    A, N, M = A2, M, N

def rotate_clockwise() :
    global A
    A2 = [[0]*M for _ in range(N)]
    for x in range(N//2) :
        for y in range(M//2) :
            A2[x][M//2+y] = A[x][y]
        for y in range(M//2, M) :
            A2[N//2+x][y] = A[x][y]
    for x in range(N//2, N) :
        for y in range(M//2):
            A2[x-N//2][y] = A[x][y]
        for y in range(M//2, M):
            A2[x][y-M//2] = A[x][y]
    A = A2

def rotate_counterclockwise() :
    global A
    A2 = [[0] * M for _ in range(N)]
    for x in range(N//2):
        for y in range(M//2):
            A2[x+N//2][y] = A[x][y]
        for y in range(M//2, M):
            A2[x][y-M//2] = A[x][y]
    for x in range(N//2, N):
        for y in range(M//2):
            A2[x][y+M//2] = A[x][y]
        for y in range(M//2, M):
            A2[x-N//2][y] = A[x][y]
    A = A2


N, M, R = map(int, input().split())
A = [input().split() for _ in range(N)]
rotate = "".join(input().split()).replace("11","").replace("22","").replace("34","").replace("43","").replace("4444","").replace("3333","").replace("56","").replace("65","").replace("5555","").replace("6666","")

for r in rotate :
    if r == '1' :
        up_and_down()
    elif r == '2' :
        left_and_right()
    elif r == '3' :
        rotate_right_90()
    elif r == '4' :
        rotate_left_90()
    elif r == '5' :
        rotate_clockwise()
    elif r == '6' :
        rotate_counterclockwise()

for x in range(N) :
    print(" ".join(A[x]))