'''
미친아두이노
https://www.acmicpc.net/problem/8972
'''
dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [-1,0,1,-1,0,1,-1,0,1]

def is_not_wall(x, y) :
    global R, C
    if x < 0 or x >= R : return False
    if y < 0 or y >= C : return False
    return True

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
move = list(map(int, list(input())))

crazy = []
tx, ty = 0, 0
for x in range(R) :
    for y in range(C) :
        if board[x][y] == '.' : continue
        if board[x][y] == 'I' :
            tx, ty = x, y
        else :
            crazy.append([x, y])

win = True
move_count = 0 
while move :
    board[tx][ty] = '.'
    d = move.pop(0)-1
    tx += dx[d]
    ty += dy[d]
    move_count += 1

    if board[tx][ty] == 'R' : 
        win = False
        break
    board[tx][ty] = 'I'

    new_crazy = []
    for _ in range(len(crazy)) :
        x, y = crazy.pop(0)
        board[x][y] = '.'
        min_dist, nx, ny = R*C, x, y
        for i in range(9) :
            if i == 4 or not is_not_wall(x+dx[i], y+dy[i]) : continue
            dist = abs(x+dx[i]-tx)+abs(y+dy[i]-ty)
            if dist < min_dist :
                min_dist, nx, ny = dist, x+dx[i], y+dy[i]

        if board[nx][ny] == 'I' :
            win = False
            break
        new_crazy.append([nx, ny])

    if not win : break

    while new_crazy :
        x, y = new_crazy.pop(0)

        overlay, i = False, 0
        while i < len(new_crazy) :
            x2, y2 = new_crazy[i]
            if x2 == x and y2 == y :
                new_crazy.pop(i)
                overlay = True
                continue
            i += 1
        
        if not overlay :
            crazy.append([x, y])
            board[x][y] = 'R'

if win :
    for x in range(R) :
        print(''.join(board[x]))
else :
    print('kraj {}'.format(move_count))
