"""
파이프옮기기1
https://www.acmicpc.net/problem/17070
"""
"""
[시간초과] 
- 이동 경로 배열 dx, dy를 사용하는 건 사치 임
"""
# pipe_type : 가로(0), 세로(1), 오른쪽 아래 대각선(2)
def move_pipe(x, y, pipe_type) :
    if x == N-1 and y == N-1 :
        global result
        result += 1
    else :
        # 가로 이동
        if pipe_type != 1 and y+1 < N and board[x][y+1] == 0:
            move_pipe(x, y+1, 0) 
        # 세로 이동
        if pipe_type != 0 and x+1 < N and board[x+1][y] == 0:
            move_pipe(x+1, y, 1) 
        # 대각선 이동
        if x+1 < N and y+1 < N and board[x+1][y+1] == 0 and board[x+1][y] == 0 and board[x][y+1] == 0 :
            move_pipe(x+1, y+1, 2) 

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

result = 0
move_pipe(0,1,0)
print(result)


"""
16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
