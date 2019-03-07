"""
1211.Ladder2
- 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서,
  모든 출발점을 검사하여 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성하라.
"""
import sys
sys.stdin = open('input.txt', 'r')

def ladder(x,y, status = 'down') :
    # 도착이라면
    if x == 99:
        return 1
    # 왼쪽
    if status != 'right' and path[x][y-1] == 1 :
        return 1 + ladder(x, y-1, "left")
    # 오른쪽
    elif status != 'left' and path[x][y+1] == 1 :
        return 1+ ladder(x,y+1, "right")
    # 아래
    return 1+ ladder(x+1,y)

for _ in range(10):
    test_case = int(input())
    path = [ [0]+list(map(int, input().split()))+[0] for _ in range(100) ]

    minPath = 0
    maxStart = 0
    for y in range(1,101) :
        if path[0][y] == 1 :
            # 탐색 함수 호출
            pathNum = ladder(0,y)
            if minPath == 0 or minPath >= pathNum :
                minPath = pathNum
                maxStart = y-1

    print('#{} {}'.format(test_case, maxStart))