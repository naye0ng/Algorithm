"""
홈 방범 서비스
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
import collections

def isNotWall(N,x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def service(N, k, x, y) :
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True

    cnt, t = 0, 1
    if house[x][y] == 1 :
        cnt +=1
    queue = collections.deque([[x,y,t]])
    while queue :
        x,y,t = queue.popleft()
        if t == k :
            break
        for i in range(4) :
            if isNotWall(N, x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] == False :
                visited[x+dx[i]][y+dy[i]] = True
                queue.append([x+dx[i], y+dy[i], t+1])
                if house[x+dx[i]][y+dy[i]] == 1 :
                    cnt += 1

    # if k == 20 :
    #     print("=============", k, x, y)
    #     for i in range(N) :
    #         print(visited[i])
    return cnt

T = int(input())
for test_case in range(1,T+1) :
    N, M = map(int, input().split())
    house = [ list(map(int, input().split())) for _ in range(N)]
    
    maxCnt = 0
    
    for k in range(1,N+2) :
        cost = k*k+(k-1)*(k-1)
        for x in range(N) :
            for y in range(N) :
                cnt = service(N, k, x, y)
                if cost <= cnt*M and maxCnt < cnt :
                    maxCnt = cnt

    print('#{} {}'.format(test_case, maxCnt))
"""
1
20 3
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""