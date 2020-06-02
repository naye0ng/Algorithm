"""
낚시왕
https://www.acmicpc.net/problem/17143
"""
def is_wall(x,y) :
    if x < 0 or x >= R :
        return True
    if y < 0 or y >= C :
        return True
    return False

# [위,오,아,왼]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

R, C, M = map(int, input().split())
board = [[-1]*C for _ in range(R)]

"""
[시간초과]
- r, c를 shark 배열에 안 넣는 것도 방법
"""
shark = [[] for _ in range(M)]
for i in range(M) :
    r, c, s, d, z = map(int, input().split())
    if d == 3 :
        d = 2
    elif d == 2 :
        d = 3
    shark[i] = [r-1,c-1,s,d-1,z]
    board[r-1][c-1] = i

# [1] 낚시왕 이동
weight = 0
for y in range(C) :
    # [2] 땅과 제일 가까운 상어 잡기
    for x in range(R) :
        if board[x][y] >= 0 :
            weight += shark[board[x][y]][4]
            shark[board[x][y]][0] = -1  # 죽음 표시
            board[x][y] = -1
            break
    # [3] 상어 이동
    new_board = [[-1]*C for _ in range(R)]
    for i in range(len(shark)) :
        if shark[i][0] == -1 :
            continue

        r, c, s, d, z = shark[i]
        for _ in range(s) :
            if is_wall(r+dx[d], c+dy[d]) :
                d = (d+2)%4
            r += dx[d]
            c += dy[d]
        shark[i] = [r, c, s, d, z]

        # [4] 잡아먹기 + 표시
        if new_board[r][c] == -1 :
            new_board[r][c] = i
        elif z > shark[new_board[r][c]][4] :
            # 자신보다 작으면 잡아먹기
            shark[new_board[r][c]][0] = -1
            new_board[r][c] = i
        else :
            # 자신이 잡아먹힘
            shark[i][0] = -1
    board = new_board
print(weight)


