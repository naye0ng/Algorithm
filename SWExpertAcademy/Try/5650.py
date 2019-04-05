"""
5650.핀볼 게임
"""
import sys
sys.stdin = open('input.txt','r')

# 위0, 왼2, 아1, 오3
dx = [-1,0, 1, 0]
dy = [0,-1,0, 1]

def movetoNext(x,y,d) :
    if x==0 and d == 2 :
        return

def isWall(x,y) :
    if x < 0 or x >= N : return True
    if y < 0 or y >= N : return True
    if arr[x][y] != 0 : return True
    return False

def move(x,y,d) :
    X, Y, count = x, y, 0
    # while True :
    #     # 처음위치로 돌아오거나 블랙홀에 빠진경우
    #     if (x==X and y==Y) and count > 0 or arr[x][y] == -1 :
    #         break
    #     # 이벤트가 발생할 때까지 최대한 이동
    while not isWall(x,y) :
        x += dx[d]
        y += dy[d]

        # 벽이면
        if x < 0 or x >= N:
            count += 1
            d = (d + 2) % 4
        if y < 0 or y >= N:
            count += 1
            d = (d + 2) % 4

        # 처음위치로 돌아오거나 블랙홀에 빠진경우
        if ((x==X and y==Y) and count > 0) or arr[x][y] == -1 :
            break
        # 웜홀이면
        if arr[x][y] != 0 :
            pass



        # 최대한 이동한 값이



T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]



    result = 0

    print('#{} {}'.format(test_case, result))