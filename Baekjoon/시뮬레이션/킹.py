'''
킹
https://www.acmicpc.net/problem/1063
'''
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

def get_position(p) :
    return [8-int(p[1]), ord(p[0])-65]

def is_wall(x, y) :
    if x < 0 or x >= 8 : return True
    if y < 0 or y >= 8 : return True
    return False

def get_direction(d) :
    if d == 'R' : return 0
    if d == 'L' : return 1
    if d == 'B' : return 2
    if d == 'T' : return 3
    if d == 'RT' : return 4
    if d == 'LT' : return 5
    if d == 'RB' : return 6
    if d == 'LB' : return 7

K, S, N = input().split()
board = [[chr(y)+str(x) for y in range(65, 73)] for x in range(8,0,-1)]

king = get_position(K)
stone = get_position(S)
for _ in range(int(N)) :
    x, y = king
    x2, y2 = stone

    d = get_direction(input())
    if is_wall(x+dx[d], y+dy[d]) : continue
    if x+dx[d] == x2 and y+dy[d] == y2 :
        if is_wall(x2+dx[d], y2+dy[d]) : continue
        stone = [x2+dx[d], y2+dy[d]]
    king = [x+dx[d], y+dy[d]]

print(board[king[0]][king[1]])
print(board[stone[0]][stone[1]])


        
        

