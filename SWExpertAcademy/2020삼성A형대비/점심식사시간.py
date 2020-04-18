"""
점심식사시간
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl
"""


def get_stair_number(n) :
    if n == N :
        global result
        visited = [False]*len(people)
        stair_state = [[[] for i in range(2)]for _ in range(2)]
        t = 0
        while t < result :
            if sum(visited) == len(people) :
                result = min(t, result)
                break
            # [1] 계단 위에 있는 사람들은 한칸씩 내려가기 >> 완료하면 visited 체크
            for s in range(2) :
                for i in range(len(stair_state[s][0])-1,-1,-1) :
                    stair_state[s][0][i][1] -= 1
                    if stair_state[s][0][i][1] == 0 :
                        visited[stair_state[s][0][i][0]] = True
                        stair_state[s][0].pop(i)

            # [2] 계단에 사람 수가 3보다 적으면 대기하는 사람들 계단에 올리기
            for s in range(2) :
                p = 3-len(stair_state[s][0])
                for _ in range(p) :
                    if stair_state[s][1] :
                        stair_state[s][0].append([stair_state[s][1].pop(0), stair[s][2]])

            # [3] 해당 시간에 도착하는 사람들 대기실로 이동
            if t < N*N :
                for s in range(2) :
                    for n in arrival_time[t][s] :
                        stair_state[s][1].append(n)
            t += 1      
    else :
        # n번째 사람이 s번째 계단에 도착
        for s in range(2) :
            t = abs(stair[s][0]-people[n][0])+abs(stair[s][1]-people[n][1])
            arrival_time[t][s].append(n)
            get_stair_number(n+1)
            arrival_time[t][s].pop()

T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000

    people, stair = [], []
    for x in range(N) :
        for y in range(N) :
            if board[x][y] == 1 :
                people.append([x,y])
            elif board[x][y] > 1 :
                stair.append([x,y,board[x][y]])

    # t 시간에 1번 2번 계단에 도착하는 사람
    arrival_time = [[[] for s in range(2)] for t in range(N*N)]
    get_stair_number(0)

    print('#{} {}'.format(test_case,result))


"""
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
"""