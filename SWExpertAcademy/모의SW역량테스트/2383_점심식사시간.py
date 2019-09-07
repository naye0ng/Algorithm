"""
2383 - 점심 식사시간
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&categoryId=AV5-BEE6AK0DFAVl&categoryType=CODE#none
"""

# 모든 경로 구해서 stair까지의 거리 구하기
def getPath(P, depth, path) :
    if depth == P :
        # 계단까지의 거리 구하기
        dists = [0]*P
        for i in range(P) :
            dists[i] = [abs(people[i][0]-stair[path[i]][0])+abs(people[i][1]-stair[path[i]][1]), path[i]]
        # [거리, 계단]으로 저장됨
        # 굳이 안해도 됨
        # dists.sort()
        l1, l2 = board[stair[0][0]][stair[0][1]], board[stair[1][0]][stair[1][1]]
        queue1 = [0]*l1
        queue2 = [0]*l2
        wait1 = 0
        wait2 = 0

        t = 1
        out = 0
        global result
        while out < P :
            if result <= t : 
                break
            # [1] 한칸씩 땡기기, 나오는 수만큼 더하기
            temp = 0
            for i in range(l1-1,-1,-1) :
                queue1[i], temp = temp, queue1[i]
            out += temp
            temp = 0
            for i in range(l2-1,-1,-1) :
                queue2[i], temp = temp, queue2[i]
            out += temp
            
            # [2] 기다리는 사람을 넣어주기
            s1 = 3-sum(queue1)
            # 들어갈 자리가 존재, 
            if s1 > 0 : 
                # 대기가 들어갈 수 있는 자리보다 작거나 같다면
                if wait1 <= s1 :
                    queue1[-1] = wait1
                    wait1 = 0
                # 더 크다면
                else :
                    queue1[-1] = s1
                    wait1 -= s1
            s2 = 3-sum(queue2)
            if s2 > 0 : 
                if wait2 <= s2 :
                    queue2[-1] = wait2
                    wait2 = 0
                else :
                    queue2[-1] = s2
                    wait2 -= s2

            # [3] 계단에 도착하면 기다리는 곳에 넣기
            #  여기도 전역 sort()후에 이곳에서 연산 처리 가능
            for dist in dists :
                # [거리, 계단]
                d, s = dist
                if d == t :
                    if s == 0 :
                        wait1 += 1
                    else :
                        wait2 += 1
            t += 1
        # print(out, t)
        if out == P :
            result = t-1
    else :
        for i in range(2) :
            getPath(P, depth+1, path+[i])

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    for x in range(N) :
        for y in range(N) :
            if board[x][y] == 1 :
                people.append([x,y])
            if board[x][y] >= 2 :
                stair.append([x, y])
    result = 120
    getPath(len(people),0,[])
    print('#{} {}'.format(test_case,result))