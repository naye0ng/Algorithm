"""
한번 쏘면 멈출 수 없어
https://www.acmicpc.net/problem/3991
"""
def isWall(x,y) :
    global h, w
    if x < 0 or x >= h :
        return True
    if y < 0 or y >= w :
        return True
    return False

dx = [0, 1, 0, 1]
dy = [1, 0, -1, 0]
# 'ㄹ' 채우기
def full(c) :
    global h, w
    x, y, i, k = 0, 0, 0, 0
    while  not isWall(x,y) :
        if color[k] == 0 :
            k += 1
        board[x][y] = str(k+1)
        color[k] -= 1
        # 다음 x,y
        if i%2 or isWall(x+dx[i],y+dy[i]) :
            i = (i+1)%4
        x += dx[i]
        y += dy[i]
        
h, w, c = map(int, input().split())
color = list(map(int,input().split()))
board = [[0]*w for _ in range(h)]
full(c) 
for i in range(h) :
    print("".join(board[i]))



