"""
배열돌리기
https://www.acmicpc.net/problem/17406
"""
import copy
import itertools

result = -1

# 시계방향 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate_clockwise(x, y, size, target):
    if size <= 1:
        getMin(target)
    else:
        temp = target[x][y]
        i = 0
        while i < 4:
            for _ in range(size-1):
                x += dx[i]
                y += dy[i]
                target[x][y], temp = temp, target[x][y]
            i += 1
        rotate_clockwise(x+1, y+1, size-2, target)

# 행 계산


def getMin(target):
    global result
    L = len(target)
    for x in range(L):
        localSum = 0
        for y in range(L):
            localSum += target[x][y]
            if localSum >= result and result > -1:
                break
        if localSum < result or result == -1:
            result = localSum

# N, M, K = map(int, input().split())
# arr = [ list(map(int, input().split())) for _ in range(N)]
# rcs = [ list(map(int, input().split())) for _ in range(K)]
# for i in range(K) :
#     rotate_clockwise(rcs[i][0]-rcs[i][2]-1,rcs[i][1]-rcs[i][2]-1,(rcs[i][0]+rcs[i][2])-(rcs[i][0]-rcs[i][2])+1,copy.deepcopy(arr))
# print(result)

mypermuatation =  itertools.permutations(mylist)
for i in mypermuatation:
    print i
