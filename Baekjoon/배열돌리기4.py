"""
배열돌리기4
https://www.acmicpc.net/problem/17406
"""
import copy

result = -1

# 시계방향 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate_clockwise(x, y, size, target):
    if size <= 1:
        return target
    else:
        temp = target[x][y]
        i = 0
        while i < 4:
            for _ in range(size-1):
                x += dx[i]
                y += dy[i]
                target[x][y], temp = temp, target[x][y]
            i += 1
        return rotate_clockwise(x+1, y+1, size-2, target)

# 행 계산
def getMin(N, M, target):
    global result
    for x in range(N) :
        localSum = 0
        for y in range(M) :
            localSum += target[x][y]
            if result != -1 and localSum > result :
                break
        if result == -1 or localSum < result  :
            result = localSum

def DFS(N, M, K,rcs,target) :
    if sum(visited) == K :
        getMin(N, M, target)
    for i in range(K) :
        if not visited[i] :
            visited[i] = 1
            DFS(N, M, K,rcs,rotate_clockwise(rcs[i][0]-rcs[i][2]-1,rcs[i][1]-rcs[i][2]-1,(rcs[i][0]+rcs[i][2])-(rcs[i][0]-rcs[i][2])+1,copy.deepcopy(target)))
            visited[i] = 0


N, M, K = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]
rcs = [ list(map(int, input().split())) for _ in range(K)]
visited = [ 0 for _ in range(K)]
DFS(N, M, K,rcs,arr)
print(result)
