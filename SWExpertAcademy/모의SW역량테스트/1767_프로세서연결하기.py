"""
프로세서연결하기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
- 문제 : 초기화를 잘하자!!!!!
"""
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def isNotWall(N,x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def connect_core(N, d, queue, core, length) :
    global maxCore
    if not queue :
        global minLength
        if core > maxCore :
            maxCore = core
            minLength = length
        elif core == maxCore :
            minLength = min(minLength, length)
    elif (core + len(queue)) >= maxCore :
        # d에 맞춰서 상좌하우로 이동
        x, y = queue.pop(0)
        x2, y2 = x+dx[d], y+dy[d]
        connected, L  = True, 0

        while isNotWall(N, x2, y2) :
            if  board[x2][y2] != 0 :
                connected =  False
                break
            board[x2][y2] = -1  # visited 체크
            L += 1 # 길이 체크
            x2 += dx[d]
            y2 += dy[d]

        # 전체 영역 확인
        for i in range(4) :
            if connected :
                connect_core(N,i,queue,core+1,length+L)
            else :
                connect_core(N,i,queue,core,length)

        # 되돌리기
        queue.insert(0,[x,y])
        d2 = (d+2)%4
        x2+=dx[d2]
        y2+=dy[d2]
        while isNotWall(N, x2, y2) :
            if  board[x2][y2] != -1 :
                break
            board[x2][y2] = 0
            x2 += dx[d2]
            y2 += dy[d2]

T = int(input())
for test_case in range(1,1+T) :
    maxCore, minLength = 0, 144
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    queue = []
    for x in range(1,N-1):
        for y in range(1,N-1):
            if board[x][y] == 1 :
                queue.append([x,y])

    for d in range(4) :
        connect_core(N, d, queue, 0, 0)
    if maxCore == 0 :
        minLength = 0
    print("#{} {}".format(test_case, minLength))
