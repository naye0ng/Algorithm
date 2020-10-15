'''
줄기세포배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]
T = int(input())
for test_case in range(1, T+1) :
    N, M, K = map(int, input().split())
    board = [[[K+1, 0] for i in range(M+2*K)] for _ in range(N+2*K)]

    t = 0
    inactive = []
    active = []
    for x in range(N) :
        cells = list(map(int, input().split()))
        for y in range(M) :
            if cells[y] == 0 : continue
            inactive.append([K+x, K+y, cells[y], cells[y]]) # x, y, 비활성, 활성
            board[K+x][K+y] = [t, cells[y]]

    while t < K :
        # 비활성인 애들 처리
        for i in range(len(inactive)) :
            inactive[i][2] -= 1

        # 활성인 애들 번식 및 죽음 처리
        for i in range(len(active)-1, -1, -1) :
            x, y = active[i][0], active[i][1]
            power = board[x][y][1]
            # 처음 1번만 번식
            if power == active[i][3] :
                for d in range(4) :
                    t2, p2 = board[x+dx[d]][y+dy[d]]
                    if t2 < t : continue
                    if t2 > t :
                        board[x+dx[d]][y+dy[d]] = [t, power]
                        inactive.append([x+dx[d], y+dy[d], power, power])
                    if t2 == t and power > p2 :
                        board[x+dx[d]][y+dy[d]] = [t, power]
                        for j in range(len(inactive)) :
                            if inactive[j][0] == x+dx[d] and inactive[j][1] == y+dy[d] :
                                inactive[j] = [x+dx[d], y+dy[d], power, power]
                                break
            active[i][3] -= 1

        # 다음 상태에서, 죽거나 활성이 되는 애들 처리
        for i in range(len(inactive)-1, -1, -1) :
            if inactive[i][2] : continue
            active.append(inactive.pop(i))

        for i in range(len(active)-1, -1, -1) :
            if active[i][3] != 0 : continue
            active.pop(i)

        t += 1

    print('#{} {}'.format(test_case, len(active)+len(inactive)))