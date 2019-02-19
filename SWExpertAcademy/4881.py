"""
4881.배열 최소 합
"""
# x번째 행에서 특정 값을 선택함
def backtrack(x, sum) :
    global n, minSum
    # 마지막 행까지 도착한 경우, 최소값보다 작은 경우만 옴
    if x == n :
        minSum = sum
    else :
        for y in range(n) :
            # 방문한적 없는 열
            if visited[y] == 0 :
                # 자신을 더해도 값이 최소값보다 작을 경우만 자신을 더한다.
                if sum + values[x][y] <= minSum :
                    # 방문 표시
                    visited[y] = 1
                    backtrack(x+1,sum+values[x][y])

                # for문 안에서 다음에 체크 될 것을 위해 복구
                visited[y] = 0


T = int(input()) 
for test_case in range(1,T+1) :
    
    n = int(input())
    values = [ list(map(int,input().split())) for _ in range(n) ]

    visited = [0]*n
    minSum = 99999
    
    backtrack(0,0)
    print(f'#{test_case} {minSum}')