'''
로봇 시뮬레이션
https://www.acmicpc.net/problem/2174
'''
D = {'W': 0, 'N':1, 'E':2, 'S':3}
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_wall(x, y) :
    if x < 0 or x >= A : return True
    if y < 0 or y >= B : return True
    return False

A, B = map(int, input().split())
N, M = map(int, input().split())

board = [[0]*B for _ in range(A)]
robot = [0]*(N+1)
for number in range(1, N+1) :
    x, y, d = input().split()
    x = int(x)-1
    y = int(y)-1
    board[x][y] = number
    robot[number] = [x, y, D[d]]

success = True
orders = [input().split() for _ in range(M)]

for number, order, count in orders :
    number = int(number)
    count = int(count)

    while count :
        count -= 1
        x, y, d = robot[number]
        if order == 'L' :
            robot[number][2] = (d-1)%4
            continue
        
        if order == 'R' :
            robot[number][2] = (d+1)%4
            continue

        if is_wall(x+dx[d], y+dy[d]) : 
            success = False
            print('Robot {} crashes into the wall'.format(number))
            break

        if board[x+dx[d]][y+dy[d]] :
            success = False
            print('Robot {} crashes into robot {}'.format(number, board[x+dx[d]][y+dy[d]]))
            break
        
        board[x][y] = 0
        board[x+dx[d]][y+dy[d]] = number
        robot[number] = [x+dx[d], y+dy[d], d]
        
    if not success : break

if success :
    print('OK')
        