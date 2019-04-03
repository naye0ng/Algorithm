"""
2819.격자판의 숫자 이어 붙이기
"""
import sys
sys.stdin = open('input.txt','r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isNotWall(x,y) :
    if x < 0 or x >=4 : return False
    if y < 0 or y >=4 : return False
    return True

def make(x,y,t) :
    if len(t) == 7 :
        result.add(t)
    else :
        for i in range(4) :
            if isNotWall(x+dx[i],y+dy[i]) :
                make(x+dx[i],y+dy[i],t+arr[x+dx[i]][y+dy[i]])

T = int(input())
for test_case in range(1,1+T) :
    arr = [input().split() for _ in range(4)]
    result = set()

    for x in range(4) :
        for y in range(4) :
            make(x,y,arr[x][y])

    print('#{} {}'.format(test_case, len(result)))