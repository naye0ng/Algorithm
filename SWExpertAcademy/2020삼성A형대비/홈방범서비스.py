"""
홈방범서비스
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def security_service(x, y, K) :
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    queue = []
    queue.append([x, y, 1])
    visited[x][y] = True
    cnt += city[x][y]

    while queue :
        x, y, k = queue.pop(0)
        if k < K :
            for i in range(4) :
                if is_not_wall(x+dx[i],y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                    queue.append([x+dx[i],y+dy[i], k+1])
                    visited[x+dx[i]][y+dy[i]] = True
                    cnt += city[x+dx[i]][y+dy[i]]
    return cnt

T = int(input())
for test_case in range(1, 1+T) :
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N) :
        for y in range(N) :
            K = N
            if N%2 == 0 :
                K = N+1
            for k in range(1, 1+K) :
                cnt = security_service(x, y, k)
                # 손해보지 않을 경우
                if cnt*M-(k*k+(k-1)*(k-1)) >= 0:
                    result = max(result, cnt)
                
    print('#{} {}'.format(test_case, result))
