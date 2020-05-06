"""
벽돌깨기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
"""
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= H :
        return False
    if y < 0 or y >= W :
        return False
    return True

def crush_blocks(ball, board) :
    queue = []
    for b in ball :
        # 맨 꼭대기 값
        for x in range(H) :
            if board[x][b] :
                queue.append([x,b,board[x][b]])
                board[x][b] = 0
                break
        # 터트리기
        while queue :
            x, y, n = queue.pop(0)
            for i in range(1, n) :
                for d in range(4):
                    if is_not_wall(x+dx[d]*i, y+dy[d]*i) and board[x+dx[d]*i][y+dy[d]*i]:
                        queue.append([x+dx[d]*i,y+dy[d]*i,board[x+dx[d]*i][y+dy[d]*i]])
                        board[x + dx[d]*i][y + dy[d]*i] = 0
        # 블록 떨어지기
        for y in range(W) :
            for x in range(H-1,-1,-1) :
                if board[x][y] == 0 :
                    for x2 in range(x-1, -1, -1) :
                        if board[x2][y] :
                            board[x][y], board[x2][y] = board[x2][y], board[x][y]
                            break
    result = 0
    for x in range(H) :
        for y in range(W) :
            if board[x][y] :
                result += 1
    return result

def drop_ball(n, ball) :
    if n == N :
        global result
        result = min(result, crush_blocks(ball,copy.deepcopy(board)))
    else :
        for i in range(W) :
            drop_ball(n+1, ball+[i])

T = int(input())
for test_case in range(1, 1+T) :
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    result = W*H
    drop_ball(0, [])

    print('#{} {}'.format(test_case, result))