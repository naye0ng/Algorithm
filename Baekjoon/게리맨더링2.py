"""
게리맨더링2
https://www.acmicpc.net/problem/17779
"""
def isNotWall(x,y) :
    global N 
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

# [2] 경계선 및 5번 선거구 만들기
def make5(x,y,d1,d2) :
    # 5번 선거구
    sum1, sum2, sum3, sum4, sum5 = 0, 0, 0, 0, 0
    for d in range(d1+1) :
        if visited[x+d-1][y-d-1] == 0 :
            visited[x+d-1][y-d-1] = 5
            sum5 += board[x+d-1][y-d-1] 
        if visited[x+d2+d-1][y+d2-d-1] == 0 :
            visited[x+d2+d-1][y+d2-d-1] = 5
            sum5 += board[x+d2+d-1][y+d2-d-1]

    for d in range(d2+1) :
        if visited[x+d-1][y+d-1] == 0 :
            visited[x+d-1][y+d-1] = 5
            sum5 += board[x+d-1][y+d-1]
        if visited[x+d1+d-1][y-d1+d-1] == 0 :
            visited[x+d1+d-1][y-d1+d-1] = 5 
            sum5 += board[x+d1+d-1][y-d1+d-1]
    
    for i in range(N) :
        s, e, is_five = 0, 0, False
        for j in range(N) :
            if visited[i][j] == 5 :
                if is_five :
                    e = j
                else :
                    # 시작
                    s = j
                    is_five = True
        if e :
            for k in range(s+1,e) :
                visited[i][k] = 5
                sum5 += board[i][k]
            

    # 1번 선거구 : 1 ≤ r < x+d1, 1 ≤ c ≤ y
    for r in range(1,x+d1) :
        for c in range(1,y+1) :
            if visited[r-1][c-1]== 0 :
                visited[r-1][c-1] = 1
                sum1 += board[r-1][c-1]
    # 2번 선거구 : 1 ≤ r ≤ x+d2, y < c ≤ N
    for r in range(1,x+d2+1) :
        for c in range(y+1,N+1) :
            if visited[r-1][c-1] == 0 :
                visited[r-1][c-1] = 2
                sum2 += board[r-1][c-1]
    # 3번 선거구 : x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    for r in range(x+d1, N+1) :
        for c in range(1,y-d1+d2) :
            if visited[r-1][c-1] == 0 :
                visited[r-1][c-1] = 3
                sum3 += board[r-1][c-1]
    # 4번 선거구 : x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    for r in range(x+d2+1,N+1) :
        for c in range(y-d1+d2, N+1) :
            if visited[r-1][c-1] == 0 :
                visited[r-1][c-1] = 4
                sum4 += board[r-1][c-1]

    return max(sum1, sum2, sum3, sum4, sum5) - min(sum1, sum2, sum3, sum4, sum5)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result = 100000000
# [1] 경계 및 기준 점 구하기
for d1 in range(1,N) :
    for d2 in range(1, N) :
        for x in range(1, N-(d1+d2)+1) :
            for y in range(1+d1, N-d2+1) :
                if d1+d2+x <= N :
                    visited = [[0]*N for _ in range(N)]
                    result = min(result,make5(x,y,d1,d2))
                    
print(result)
            
"""
7
1 2 3 4 1 6 3
7 8 9 1 4 2 3
2 3 4 1 1 3 3
6 6 6 6 9 4 3
9 1 9 1 9 5 3
1 1 1 1 9 9 3
1 1 1 1 9 9 3
"""