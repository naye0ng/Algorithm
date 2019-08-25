"""
톱니바퀴
https://www.acmicpc.net/problem/14891
"""

def moveClock(g) :
    temp = gears[g][-1]
    for i in range(8) :
        gears[g][i], temp = temp, gears[g][i]

def moveNonClock(g) :
    temp = gears[g][0]
    for i in range(7,-1,-1) :
        gears[g][i], temp = temp, gears[g][i]

def moveGear(gear, direction, before) :
    # 기어의 오른쪽
    if before != 1 and gear+1 < 4 and (gears[gear][2] + gears[gear+1][6]) == 1 :
        moveGear(gear+1,direction*(-1),2)
    # # 기어의 왼쪽
    if before != 2 and gear-1 >= 0 and (gears[gear][6] + gears[gear-1][2]) == 1 :
        moveGear(gear-1,direction*(-1),1)
    # # 현재 기어 회전
    if direction == 1 :
        moveClock(gear)
    else :
        moveNonClock(gear)

gears = [list(map(int, " ".join(input()).split())) for _ in range(4)]
K = int(input())

for _ in range(K) :
    gear, direction = map(int, input().split())
    moveGear(gear-1, direction, 0) 

print(gears[0][0]*1+gears[1][0]*2+gears[2][0]*4+gears[3][0]*8)



"""
10101111
01111101
11001110
00000010
2
3 -1
1 1
"""