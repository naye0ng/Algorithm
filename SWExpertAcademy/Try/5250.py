"""
5250.최소비용

- 모든 지점을 거치지 않음, 감소하는 가중치가 없다 => 다익스트라
"""
import sys
sys.stdin = open('input.txt','r')

import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isWall(x,y) :
    if x < 0 or x >= N :
        return True
    if y < 0 or y >= N :
        return True
    return False

def dijstra(x,y) :
    # 현재 점 방문
    visited[N*x+y] = 1
    # 위, 아, 왼, 오 연관 점 => D
    heap = []
    for i in range(4) :
        if not isWall(x+dx[i],y+dy[i]) :
            next = N*(x+dx[i])+y+dy[i]
            if A[x][y] < A[x+dx[i]][y+dy[i]] :
                D[next] = 1+(A[x+dx[i]][y+dy[i]]-A[x][y])
            else :
                D[next] = 1
            heapq.heappush(heap, [D[next], next])
    v =1
    while v < N*N :
        #방문하지 않은 점들 중 가중치가 가장 작은 값
        # w, mini = 0, 99999
        # for i in range(N*N) :
        #     if not visited[i] and mini >= D[i] :
        #         mini = D[i]
        #         w = i
        w = heapq.heappop(heap)[1]

        visited[w] = 1
        x, y = w//N, w%N
        # w와 연관된 곳 조사
        # 다음 후보 만들기
        heap = []
        for i in range(4):
            if not isWall(x + dx[i], y + dy[i]):
                temp = 1
                if A[x][y] < A[x + dx[i]][y + dy[i]]:
                    temp += (A[x + dx[i]][y + dy[i]] - A[x][y])
                next = N*(x+dx[i])+y+dy[i]
                D[next] = min(D[N*(x+dx[i])+y+dy[i]],D[N*x+y]+temp)
                # 다음 후보군
                if not visited[next] :
                    heapq.heappush(heap,[D[next],next])
        v+=1
    return D[-1]

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    D = [99999]*(N*N)
    visited = [0]*(N*N)

    print('#{} {}'.format(test_case, dijstra(0,0)))