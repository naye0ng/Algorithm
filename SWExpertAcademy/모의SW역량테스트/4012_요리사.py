"""
4012 - 요리사
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE
"""

def cooking(N,depth,k) :
    if depth == N//2 :
        A, B = [], []
        for i in range(N) :
            if visited[i] :
                A.append(i)
            else :
                B.append(i)
        # 계산하기
        sA, sB = 0, 0
        for x in range(N//2-1) :
            for y in range(x+1,N//2) :
                sA += synergy[A[x]][A[y]] + synergy[A[y]][A[x]]
                sB += synergy[B[x]][B[y]] + synergy[B[y]][B[x]]
        global result
        result = min(result,abs(sA-sB))
    else :
        for i in range(k,N) :
            visited[i] = True
            cooking(N,depth+1,i+1)
            visited[i] = False

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())  
    synergy = [ list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    result = 20000
    cooking(N,0,0)
    print('#{} {}'.format(test_case,result))



"""
1
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
"""