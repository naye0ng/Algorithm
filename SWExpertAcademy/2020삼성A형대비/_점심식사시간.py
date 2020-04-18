"""
점심식사시간
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl
"""
def go_to_stair(P, n) :
    if n == P :
        global result
        stair_state = [[[0]*board[stair[s][0]][stair[s][1]],[]] for s in range(2)]
        t = 0
        while t < result :
            for i in range(2) :
                # [1] 계단에 있는 애들 1칸씩 이동
                stair_state[i][0][0] = 0
                for k in range(1,len(stair_state[i][0])) :
                    stair_state[i][0][k-1], stair_state[i][0][k] = stair_state[i][0][k], stair_state[i][0][k-1]


                # [2] 대기하는 애들 계단으로 이동


            # [3] 계단에 도착하는 애들 대기
            t += 1


    else :
        # n번째 사람이 s번째 계단으로 나감
        for s in range(2) :
            people[n][2], people[n][3] = s, abs(people[n][0]-stair[s][0])+abs(people[n][1]-stair[s][1])
            go_to_stair(P, n+1)

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    people, stair = [], []

    for x in range(N) :
        for y in range(N) :
            if board[x][y] == 1 :
                # x, y, 계단번호, 계단도착시간
                people.append([x,y,0,0])
            elif board[x][y] > 1 :
                stair.append([x,y])
    result = 10000
    go_to_stair(len(people), 0)

    print('#{} {}'.format(test_case,1))


"""
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
"""