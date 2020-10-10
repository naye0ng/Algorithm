'''
벽돌깨기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE
'''
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x, y) :
    if x < 0 or x >= H : return False
    if y < 0 or y >= W : return False
    return True

def crush_remains(balls, board) :
    queue = []
    for b in balls :
        for x in range(H) :
            if board[x][b] != 0 :
                queue.append([x, b, board[x][b]])
                board[x][b] = 0
                break

        while queue :
            for _ in range(len(queue)) :
                x, y, n = queue.pop(0)
                for i in range(1, n) :
                    for d in range(4) :
                        if is_not_wall(x+dx[d]*i, y+dy[d]*i) and board[x+dx[d]*i][y+dy[d]*i]:
                            queue.append([x+dx[d]*i, y+dy[d]*i, board[x+dx[d]*i][y+dy[d]*i]])
                            board[x+dx[d]*i][y+dy[d]*i] = 0
        
        for y in range(W) :
            for x in range(H-1, -1, -1) :
                if board[x][y] != 0 : continue
                x2 = x
                for a in range(x-1, -1, -1) :
                    if board[a][y] != 0 :
                        x2 = a
                        break
                if x2 == x : break
                board[x][y], board[x2][y] = board[x2][y], board[x][y]

    remains = 0
    for x in range(H) :
        for y in range(W) :
            if board[x][y] == 0 : continue
            remains += 1
    return remains

def drop_ball(n, balls) :
    if n == N :
        global answer
        answer = min(answer, crush_remains(balls, copy.deepcopy(board)))
    else : 
        for w in range(W) :
            drop_ball(n+1, balls+[w])

T = int(input())
for test_case in range(1, 1+T) :
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    answer = W*H
    drop_ball(0, [])

    print('#{} {}'.format(test_case, answer))