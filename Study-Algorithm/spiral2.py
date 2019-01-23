"""
Spiral Algorithm
(나선형, 달팽이 알고리즘)

2. delta와 isWall()이용
"""
x, y = 0, 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir_start = 0 #delta 제어

an = [[0]*5 for i in range(5)]
n = len(an)

def isWall(x,y) :
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    if an[x][y] != 0 : return True
    return False

for i in range(1,n*n+1) :
    an[x][y] = i
    x += dx[dir_start]
    y += dy[dir_start]

    if isWall(x,y) :
        # 벽을 만나면, 이전에 더해진 값을 변경하고 델타를 증가시키자
        x -= dx[dir_start]
        y -= dy[dir_start]
        dir_start = (dir_start+1)%4
        # x,y 위치 재설정
        x += dx[dir_start]
        y += dy[dir_start] 

for e in range(n) :
    print(an[e])
