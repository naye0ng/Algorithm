"""
줄기세포배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
T = int(input())
for test_case in range(1, 1+T) :
    N, M, K = map(int, input().split())
    board = [[0]*(M+K*2) for _ in range(N+K*2)]

    T = 0
    for x in range(K, K+N) :
        y = K-1
        for n in map(int, input().split()) :
            y += 1
            if n == 0 :
                continue
            board[x][y] = [n, 0, n, T]
            
    while T < K :
        T += 1
        for x in range(N+K*2) :
            for y in range(M+K*2) :
                if board[x][y] == 0 :
                    continue
                """
                [핵심]같은 시간대에 추가된것 제외!!
                """
                if board[x][y][3] < T :
                    # 비활성
                    if board[x][y][1] == 0 :
                        board[x][y][2] -= 1
                        if board[x][y][2] == 0 :
                            board[x][y][1], board[x][y][2] = 1, board[x][y][0]
                    # 활성
                    elif board[x][y][1] == 1 :
                        for i in range(4) :
                            # 비어있거나, 같은 시간에 생성되었을 때 현재 세포가 더 크다면
                            if board[x+dx[i]][y+dy[i]] == 0 or (board[x+dx[i]][y+dy[i]][3] == T and board[x+dx[i]][y+dy[i]][0] < board[x][y][0]) :
                                board[x+dx[i]][y+dy[i]] = [board[x][y][0], 0, board[x][y][0], T]
                                
                        board[x][y][2] -= 1
                        if board[x][y][2] == 0 :
                            board[x][y][1] = 2
                            
    alive = 0
    for x in range(N+K*2) :
        for y in range(M+K*2) :
            if board[x][y] != 0 and board[x][y][1] < 2 :
                alive += 1

    print('#{} {}'.format(test_case, alive))
