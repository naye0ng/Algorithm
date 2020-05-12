"""
요리사
problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE
"""
def cook(n, k) :
    if n == N//2 :
        A, B = [], []
        for i in range(N) :
            if visited[i] :
                A.append(i)
            else :
                B.append(i)

        sA, sB = 0, 0
        for x in range(N//2-1) :
            for y in range(x+1, N//2) :
                sA += taste[A[x]][A[y]] + taste[A[y]][A[x]]
                sB += taste[B[x]][B[y]] + taste[B[y]][B[x]]

        global result
        result = min(result, abs(sA-sB))
    else :
        for i in range(k, N) :
            visited[i] = True
            cook(n+1, i+1)
            visited[i] = False

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    taste = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    result = 20000
    cook(0,0)
    print('#{} {}'.format(test_case,result))


"""
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
"""