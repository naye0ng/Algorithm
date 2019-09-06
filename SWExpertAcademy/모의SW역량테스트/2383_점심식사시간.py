"""
2383 - 점심 식사시간
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&categoryId=AV5-BEE6AK0DFAVl&categoryType=CODE#none
"""

# 계단에서부터 시간이 지날 수록, 가장 빨리 끝날 수 있도록 시작
def downStair() :
    pass

# 모든 경로 구해서 stair까지의 거리 구하기
def getPath(P, depth, path) :
    if depth == P :
        # 계단까지의 거리 구하기
        dists = [0]*P
        for i in range(P) :
            dists[i] = [abs(people[i][0]-stair[path[i]][0])+abs(people[i][1]-stair[path[i]][1]), path[i]]
        # [거리, 계단]으로 저장됨
        dists.sort()
        # 시간 계산
        queue1 = [False]*(board[stair[0][0]][stair[0][1]]+1)
        queue2 = [False]*(board[stair[1][0]][stair[1][1]]+1)
        t = 1
        while True :
        # dist를 봐서 거리가 t와 같은 애들을 넣어보자
        # 먼저 나가기 체크
            temp = False
            for i in range(len(queue1)-1) :
                queue1[i], queue1[i+1] = temp, queue1[i]
                temp = queue1

            for dist in dists :
                d, s = dist
                # 해당 시간에 계단에 도달할 수 있다면?
                if d == t :
                    if s == 0 :
                        queue1[-1] = True
                    else :
                        queue2[-1] = True



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
    getPath(len(people),0,[])
    print('{} {}'.format(test_case,1))