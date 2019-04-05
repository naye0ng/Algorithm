"""
2117.홈 방범 서비스
"""
import sys
sys.stdin = open('input.txt','r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isBlock(x,y) :
    if x < 0 or x >= N : return False
    if y < 0 or y >= N : return False
    return True

def service(x,y) :
    visited = [[0]*N for _ in range(N)]
    queue = []

    queue.append((x,y,2))
    visited[x][y] = 1

    depth, price, num, local =1, 1, 0, 0
    if arr[x][y]: local = 1
    while queue :
        x, y, k = queue.pop(0)
        if k != depth :
            # 손해가 아니라면
            if (local)*M-price >= 0 : num = local
            depth = k
            price = k*k+(k-1)*(k-1)
        for i in range(4) :
            # 방문한 적 없고 블록범위를 벗어나지 않음
            if isBlock(x+dx[i],y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                # 값이 존재한다면
                if arr[x+dx[i]][y+dy[i]]: local +=1
                visited[x + dx[i]][y + dy[i]] =1
                queue.append((x+dx[i],y+dy[i],k+1))
    return num

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(N)]

    result = 0
    for x in range(N) :
        for y in range(N) :
            temp = service(x,y)
            if temp > result : result=temp

    print('#{} {}'.format(test_case, result))