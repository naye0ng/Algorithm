"""
감시
https://www.acmicpc.net/problem/15683
"""
import copy

def isNotWall(x,y,N,M) :
    if x < N and x>= 0 :
        if y < M and y>=0 :
            return True
    return False

# 위, 오, 아, 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def checkCctv1(N,M,x,y,office,i) :
    x += dx[i]
    y += dy[i]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[i]
        y += dy[i]
    return office

def checkCctv2(N,M,x,y,office,i) :
    initX, initY = x, y
    x += dx[i]
    y += dy[i]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[i]
        y += dy[i]
    x, y = initX, initY
    x += dx[i+2]
    y += dy[i+2]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[i+2]
        y += dy[i+2]
    return office

def checkCctv3(N,M,x,y,office,i) :
    initX, initY = x, y
    x += dx[i%4]
    y += dy[i%4]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[i%4]
        y += dy[i%4]
    x, y = initX, initY
    x += dx[(i+1)%4]
    y += dy[(i+1)%4]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[(i+1)%4]
        y += dy[(i+1)%4]
    return office

def checkCctv4(N,M,x,y,office,i) :
    initX, initY = x, y
    x += dx[i%4]
    y += dy[i%4]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[i%4]
        y += dy[i%4]
    x, y = initX, initY
    x += dx[(i+1)%4]
    y += dy[(i+1)%4]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[(i+1)%4]
        y += dy[(i+1)%4]
    x, y = initX, initY
    x += dx[(i+2)%4]
    y += dy[(i+2)%4]
    while isNotWall(x,y,N,M) :
        if office[x][y] == 6 :
            break
        elif office[x][y] == 0 :
            office[x][y] = '#'
        x += dx[(i+2)%4]
        y += dy[(i+2)%4]
    return office

def checkCctv5(N,M,x,y,office) :
    initX, initY = x, y
    for i in range(4) :
        x, y = initX, initY
        x += dx[i]
        y += dy[i]
        while isNotWall(x,y,N,M) :
            if office[x][y] == 6 :
                break
            elif office[x][y] == 0 :
                office[x][y] = '#'
            x += dx[i]
            y += dy[i]
    return office

result = 100
def checkCctv(N,M,cctv,office) :
    if len(cctv) == 0 :
        # 사작지대 계산
        global result
        result = min(result,countNotSee(N,M,office))
    else :
        c = cctv.pop(0) 
        x, y = c[0], c[1]
        if office[x][y] == 1 :
            for i in range(4) :
                checkCctv(N,M,copy.deepcopy(cctv),checkCctv1(N,M,x,y,copy.deepcopy(office),i))
        elif office[x][y] == 2 :
            for i in range(2) :
                checkCctv(N,M,copy.deepcopy(cctv),checkCctv2(N,M,x,y,copy.deepcopy(office),i))
        elif office[x][y] == 3 :
            for i in range(4) :
                checkCctv(N,M,copy.deepcopy(cctv),checkCctv3(N,M,x,y,copy.deepcopy(office),i))
        elif office[x][y] == 4 :
            for i in range(4) :
                checkCctv(N,M,copy.deepcopy(cctv),checkCctv4(N,M,x,y,copy.deepcopy(office),i))
        elif office[x][y] == 5 :
            checkCctv(N,M,copy.deepcopy(cctv),checkCctv5(N,M,x,y,copy.deepcopy(office)))

def countNotSee(N,M,office) :
    count = 0
    for x in range(N) :
        for y in range(M) :
            if office[x][y] == 0 :
                count += 1
    return count



N, M = map(int, input().split())
office = [ list(map(int, input().split())) for _ in range(N)]
cctv = []
for x in range(N) :
    for y in range(M) :
        if office[x][y] >= 1 and office[x][y] <= 5 :
            cctv.append([x,y])

checkCctv(N,M,copy.deepcopy(cctv),copy.deepcopy(office))
print(result)