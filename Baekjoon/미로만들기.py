"""
미로만들기
https://www.acmicpc.net/problem/1347
"""
N = input()
M = " ".join(input()).split()

"""
      북
서          동
  R <-남-> L
"""
# 남, 동, 북, 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

minX, maxX, minY, maxY = 0,0,0,0
x, y, d = 0, 0, 0
move = []
move.append([x,y])
for m in M :
    if m == 'F' :
        x += dx[d]
        y += dy[d]
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
        move.append([x,y])
    elif m == 'R' :
        d = (d-1)%4
    elif m == 'L' :
        d = (d+1)%4

x, y = minX*(-1), minY*(-1)
board = [["#"]*(minY*(-1)+maxY+1)for _ in range(minX*(-1)+maxX+1)]

for i in range(len(move)) :
    board[x + move[i][0]][y+move[i][1]] = "."

for i in range(minX*(-1)+maxX+1) :
    print("".join(board[i]))