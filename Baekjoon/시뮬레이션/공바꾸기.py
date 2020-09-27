'''
공바꾸기
https://www.acmicpc.net/problem/10813
'''
N, M = map(int, input().split())
board = [str(ball) for ball in range(1, N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    board[a-1], board[b-1] = board[b-1], board[a-1]

print(" ".join(board))
