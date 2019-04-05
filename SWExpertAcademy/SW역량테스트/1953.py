"""
1953.탈주범 검거
"""
import sys
sys.stdin = open('input.txt','r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]
D = [[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
num = [4,2,2,2,2,2,2]
# 이동할 방향 대비 다음에 올 수 있는 파이트 번호
pipe = [[1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]]

def isWall(x,y) :
    if x < 0 or x >= N : return True
    if y < 0 or  y >= M : return True
    if visited[x][y] : return True
    return False

def move(x,y) :
    queue = []
    queue.append((x,y,1))

    count = 0
    while queue :
        x,y,t = queue.pop(0)

        if t > L : break
        if not visited[x][y] :
            visited[x][y] = 1
            count += 1

        if not arr[x][y] : continue
        # 다음 찾기
        k = num[arr[x][y]-1]
        for i in range(k) :
            a, b = x +dx[D[arr[x][y]-1][i]], y +dy[D[arr[x][y]-1][i]]
            # 다음에 들어갈 파이프 모양(arr[a][b])이 이동항 방향과 호환가능?
            if not isWall(a,b) and arr[a][b] in pipe[D[arr[x][y]-1][i]] :
                queue.append((a,b,t+1))
    return count

T = int(input())
for test_case in range(1,1+T) :
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    print('#{} {}'.format(test_case, move(R,C)))





