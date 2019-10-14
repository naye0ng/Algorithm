"""
벌꿀채취
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE
"""
# 이어져있는 M개에서의 최대값 찾기
def Honey(x, y, k, n, honey, pure) :
    global M, N, C, maxPure
    if n < M :
        for i in range(k, y+M) :
            if honey+board[x][i] <= C :
                Honey(x, y, i+1, n+1, honey+board[x][i], pure+(board[x][i]*board[x][i]))
    if maxPure < pure :
        maxPure = pure
   


T = int(input())
for test_case in range(1,T+1) :
    N, M, C = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(N)]
    queue = []
    for x in range(N) :
        for y in range(N-M+1) :
            maxPure = 0
            Honey(x, y, y, 0, 0, 0)
            queue.append([maxPure, x, y, y+M-1])
    queue.sort(reverse=True)

    # 제일 크고 겹치지 않는 값 고르기
    result, X, startY, endY = queue.pop(0)
    while queue :
        pure, x, sY, eY = queue.pop(0)
        if x != X :
            result += pure
            break
        # 범위 겹치는거 체크
        if startY < sY and startY+M <= sY :
            result += pure
            break
        elif sY < startY and sY+M <= startY :
            result += pure
            break

    print('#{} {}'.format(test_case,result))



"""
1
6 3 20
8 5 2 4 3 1
4 3 6 1 1 8
4 4 1 2 3 1
1 7 4 9 6 1
6 5 1 2 8 4
3 1 4 5 1 3


239
"""