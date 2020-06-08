"""
드래곤커브
https://www.acmicpc.net/problem/15685
"""
# →, ↑, ←, ↓
dx = [0,-1,0,1]
dy = [1,0,-1,0]

N = int(input())
"""
[주의] - 부등호 범위 제대로 읽자!!!!
격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.
즉, 101까지 설정해줘야한다!!
"""
board = [[0]*101 for _ in range(101)]

# 드래곤커브
for _ in range(N) :
    y, x, d, g = map(int, input().split())
    board[x][y] = 1

    x += dx[d]
    y += dy[d]
    board[x][y] = 1
    queue = [d]
    for i in range(g) :
        for j in range(len(queue)-1,-1,-1) :
            d = (queue[j]+1)%4
            x += dx[d]
            y += dy[d]
            board[x][y] = 1
            queue.append(d)

# 네 꼭지점 계산
result = 0
for x in range(100) :
    for y in range(100) :
        if board[x][y] and board[x+1][y] and board[x][y+1] and board[x+1][y+1] :
            result += 1

print(result)


