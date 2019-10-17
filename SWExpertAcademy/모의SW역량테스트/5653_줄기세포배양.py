"""
줄기세포 배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE
"""

dx = [-1,0,1,0]
dy = [0,-1,0,1]

T = int(input())
for test_case in range(1, 1+T) :
    N, M, K = map(int,input().split())
    board = [[0]*(M+K*2) for _ in range(N+K*2)]

    t = 0 
    for x in range(N) :
        tmp = list(map(int, input().split()))
        for y in range(M) :
            if tmp[y] :
                board[K+x][K+y] = [tmp[y],tmp[y],tmp[y], t]
    
    while t < K :
        t+= 1
        for x in range(N+K*2) :
            for y in range(M+K*2) :
                # 세포가 존재하는데 이전 시간에 추가된 경우, 살아있는 경우
                # [TIP] 이전에 이 문제를 해결하지 못했던 이유는 동일한 시간에 추가된 세포도 처리했기 떄문이라고 생각함
                if board[x][y] and board[x][y][3] != t and board[x][y][1] > 0:
                    # 비활성이라면
                    if board[x][y][0] > 0 :
                        board[x][y][0] -= 1
                    elif board[x][y][0] == 0 :
                        # 한번만 상하좌우로 확장됨
                        for i in range(4) :
                            # 빈자리, 같은 시간에 퍼진 것이면서 나보다 작은 경우
                            if board[x+dx[i]][y+dy[i]] == 0 or (board[x+dx[i]][y+dy[i]][3] == t and board[x+dx[i]][y+dy[i]][2] < board[x][y][2]) :
                                board[x+dx[i]][y+dy[i]] = [board[x][y][2],board[x][y][2],board[x][y][2],t]
                        board[x][y][0] -= 1
                        board[x][y][1] -= 1
                    # 활성이라면
                    else :
                        board[x][y][1] -= 1\

    # [2] 살아있는 세포 체크
    result = 0
    for x in range(N+K*2) :
        for y in range(M+K*2) :
            if board[x][y] and board[x][y][1] > 0 : 
                result += 1

    print('#{} {}'.format(test_case,result))