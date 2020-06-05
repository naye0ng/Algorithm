"""
배열돌리기1
https://www.acmicpc.net/problem/16926
"""

def rotate(R, k) :
    while R :
        for t in range(k) :
            temp = A[t][t]
            for x in range(t+1, N-t) :
                A[x][t], temp = temp, A[x][t]
            for y in range(t+1, M-t) :
                A[N-1-t][y], temp = temp, A[N-1-t][y]
            for x in range(N-1-t-1,t-1,-1) :
                A[x][M-1-t], temp = temp, A[x][M-1-t]
            for y in range(M-1-t-1, t-1, -1) :
                A[t][y], temp = temp, A[t][y]
        R-= 1

N, M, R = map(int, input().split())
A = [input().split() for _ in range(N)]
rotate(R, min(N,M)//2)

for x in range(N) :
    print(" ".join(A[x]))
