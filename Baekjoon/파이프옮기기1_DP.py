"""
파이프옮기기1
https://www.acmicpc.net/problem/17070
"""

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# 가로, 세로, 대각선
dp = [[[0]*3 for i in range(N)] for _ in range(N)]
dp[0][1][0] = 1

# 맨 윗줄 가로 이동
for y in range(2, N) :
    if board[0][y] :
        break
    dp[0][y][0] = 1

for x in range(1, N) :
    for y in range(2, N) :
        if not board[x][y] and not board[x-1][y] and not board[x][y-1] :
            # dp[x-1][x+1]의 모든 방향에서 들어온 값들은 대각선 이동이 가능
            dp[x][y][2] += dp[x-1][y-1][2] + dp[x-1][y-1][1] + dp[x-1][y-1][0]
        if not board[x][y] :
            # 왼쪽에서 들어올 수 있는 값 = 대각선, 왼쪽
            dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
            # 위쪽에서 들어올 수 있는 값 = 대각선, 위쪽
            dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]

print(sum(dp[N-1][N-1]))

