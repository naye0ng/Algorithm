"""
5653 - 줄기세포배양
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE
"""
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def cell(K,t,x1,y1,x2,y2) :
    # 루프를 돌면서 현재 활성이라면?
    for x in range(x1,x2) :
        for y in range(y1,y2) :
            if container[x][y] >= 1 :
                # 비활성 상태
                if visited[x][y][0] < container[x][y] :
                    visited[x][y][0] += 1
                # 활성상태
                elif visited[x][y][0] == container[x][y] and visited[x][y][1] < container[x][y] :
                    # 여기에서 변경 시작
                    for i in range(4) :
                        pass
                    visited[x][y][1] += 1
                # 죽은 상태이므로 변경
                else :
                    container[x][y] = 0
                    
                    


T = int(input())
for test_case in range(1, T+1) :
    # N, M, K = map(int, input().split())
    # [비활성, 활성]
    visited = [[0,0]*6050 for _ in range(6050)]
    container = [[0]*6050 for _ in range(6050)]
    # 3000부터 시작하는 거임
    for x in range(N) :
        row = list(map(int, input().split()))
        for y in range(M) :
            container[3000+x][3000+y] = row[y] 
    cell(K,0,3000,3000,3000+N,3000+M)
    print("#{} {}".format(test_case, 1))

"""
1
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
"""