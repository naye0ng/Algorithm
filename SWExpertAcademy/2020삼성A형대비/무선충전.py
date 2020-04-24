"""
무선충전
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
"""
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

def charged_bettery(t, charged) :
    if t <= M :
        """
        [시간초과] 선택하는 모든 경우의 수를 재귀로 다 돈다
        [해결] 최대 값을 가지는 값을 찾아서 넘기면 M번 안에 해결이 가능
        """
        max_charge = 0
        if board[path[0][t][0]][path[0][t][1]] and board[path[1][t][0]][path[1][t][1]]:
            for user1_BC in board[path[0][t][0]][path[0][t][1]] :
                for user2_BC in board[path[1][t][0]][path[1][t][1]] :
                    if user1_BC == user2_BC :
                        max_charge = max(max_charge, BC[user1_BC][3])
                    else :
                        max_charge = max(max_charge, BC[user1_BC][3]+BC[user2_BC][3])
        elif board[path[0][t][0]][path[0][t][1]] :
            if len(board[path[0][t][0]][path[0][t][1]]) == 1 :
                max_charge = max(max_charge, BC[board[path[0][t][0]][path[0][t][1]][0]][3])
            else :
                # 제일 충전 차지가 큰 값 찾기
                for bc in board[path[0][t][0]][path[0][t][1]]:
                    max_charge = max(max_charge, BC[bc][3])
        elif board[path[1][t][0]][path[1][t][1]]:
            if len(board[path[1][t][0]][path[1][t][1]]) == 1 :
                max_charge = max(max_charge, BC[board[path[1][t][0]][path[1][t][1]][0]][3])
            else :
                for bc in board[path[1][t][0]][path[1][t][1]]:
                    max_charge = max(max_charge, BC[bc][3])

        charged_bettery(t + 1, charged + max_charge)
    else :
        global result
        result = max(result, charged)

T = int(input())
for test_case in range(1, 1+T) :
    M, A = map(int, input().split())

    # 사용자 이동 경로 찾기
    user = [list(map(int, input().split())) for _ in range(2)]
    path = [[0]*(M+1) for _ in range(2)]
    path[0][0] = [0,0]
    path[1][0] = [9,9]
    for i in range(2) :
        for m in range(M) :
            path[i][m+1] = [path[i][m][0]+dx[user[i][m]],path[i][m][1]+dy[user[i][m]]]

    BC = [list(map(int, input().split())) for _ in range(A)]
    board = [[[] for i in range(10)] for _ in range(10)]

    for i in range(A) :
        board[BC[i][1]-1][BC[i][0]-1].append(i)
        queue = []
        queue.append([BC[i][1]-1,BC[i][0]-1, 0])
        visited = [ [False]*10 for _ in range(10)]
        visited[BC[i][1]-1][BC[i][0]-1] = True
        while queue :
            x, y, t = queue.pop(0)

            if t < BC[i][2] :
                for k in range(1,5) :
                    if 0 <= x+dx[k] < 10 and 0 <= y+dy[k] < 10 and not visited[x+dx[k]][y+dy[k]] :
                        visited[x + dx[k]][y + dy[k]] = True
                        board[x + dx[k]][y + dy[k]].append(i)
                        queue.append([x+dx[k],y+dy[k], t+1])

    result = 0
    charged_bettery(0,0)

    print('#{} {}'.format(test_case, result))



"""
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
"""