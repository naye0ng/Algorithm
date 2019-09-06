"""
5653 - 줄기세포배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE
"""
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def Cell(K) :
    for t in range(1, K) :
        # t시간에 활성화되는 세포들을 내림차순으로 정렬하여 생명력이 큰 값부터 처리
        queue = []
        for i in range(t//2+1,t+1) :
            queue.extend(timeGrid[i])
        queue.sort()
        n = len(queue)-1
        while n >= 0 :
            s, x, y = queue[n]
            for i in range(4) :
                if (x+dx[i], y+dy[i]) not in visited : 
                    timeGrid[t+s+1].append([s, x+dx[i], y+dy[i]])
                    visited.add((x+dx[i], y+dy[i]))
            n -= 1
    lifeCell = 0
    for i in range(K//2+1,K):
        for grid in timeGrid[i] :
            if grid[0]+i > K :
                lifeCell += 1
            else :
                break
    for i in range(K,K+11) :
        lifeCell += len(timeGrid[i])
    return lifeCell

T = int(input())
for test_case in range(1, T+1) :
    N, M, K = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(N)]
    timeGrid = { t : [] for t in range(1,K+11)}
    visited = set()
    for x in range(N):
        for y in range(M):
            if grids[x][y] > 0 :
                timeGrid[grids[x][y]].append([grids[x][y],x,y])
                visited.add((x,y))
    print("#{} {}".format(test_case, Cell(K)))

"""
1
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
"""