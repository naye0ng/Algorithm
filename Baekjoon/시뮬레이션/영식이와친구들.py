'''
영식이와 친구들
https://www.acmicpc.net/problem/1592
'''
N, M, L = map(int, input().split())
board = [0]*N

ball = 0
board[ball] += 1
count = 0
while board[ball] < M:
    if board[ball]%2 :
        ball = (ball+L)%N
    else :
        ball = (ball-L)%N
    board[ball] += 1
    count += 1

print(count)