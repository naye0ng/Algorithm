"""
5188.최소합
"""
import sys
sys.stdin = open('input.txt','r')

def move(s, x, y) :
    if x==0 and y==0 :
        s += number[x][y]
        global minS
        if minS == 0 or minS > s :
            minS = s
    else :
        # 위, 왼쪽으로 이동
        if x != 0 : move(s+number[x][y],x-1,y)
        if y != 0 : move(s+number[x][y],x,y-1)

T = int(input())
for test_case in range(1,1+T) :

    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]

    minS = 0
    move(0,N-1,N-1)

    print('#{} {}'.format(test_case, minS))