"""
특이한자석
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH
"""
def rotate(N, D) :
    visited[N] = True
    # 오른쪽, 왼쪽 바퀴
    if N-1 >= 0 and not visited[N-1] and magnet[N-1][2] != magnet[N][6] :
        rotate(N-1, -D)
    if N+1 < 4 and not visited[N+1] and magnet[N+1][6] != magnet[N][2] :
        rotate(N+1, -D)
    # 회전
    if D == 1 :
        for i in range(7,0,-1) :
            magnet[N][i], magnet[N][i-1] = magnet[N][i-1], magnet[N][i]
    else :
        for i in range(7) :
            magnet[N][i], magnet[N][i+1] = magnet[N][i+1], magnet[N][i]

T = int(input())
for test_case in range(1, 1+T) :
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K) :
        N, D = map(int, input().split())
        visited = [False]*4
        rotate(N-1, D)
    
    result = 0
    for i in range(4) :
        result += magnet[i][0]*(2**i)

    print('#{} {}'.format(test_case, result))


"""
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
"""