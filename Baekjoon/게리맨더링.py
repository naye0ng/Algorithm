"""
개리맨더링
https://www.acmicpc.net/problem/17471
"""
"""
# 이렇게 푸는 경우, 그래프가 12, 34, 56으로 연결된 것을 가려내지 못하고 다 연결된다고 판단함
def is_connect(arr) :
    if len(arr) == 1 :
        return True

    visited = [False]*len(arr)
    for a in arr :
        # i와 연결 가능한 점 모두 visited 체크
        for k in range(len(arr)) :
            if not visited[k] and path[a][arr[k]] :
                visited[k] = True

    if sum(visited) == len(arr) :
        return True
    return False
"""
# BFS로 연결을 확인해보자
def is_connect(arr) :
    if len(arr) == 1 :
        return True
    visited = [False]*len(arr)
    queue = [0] # arr의 index가 들어감
    while queue :
        idx = queue.pop(0)
        for i in range(len(arr)) :
            if not visited[i] and path[arr[idx]][arr[i]] :
                visited[i] = True
                queue.append(i)

    if sum(visited) == len(arr) :
        return True
    return False

def seperate(n,A,B) :
    if n == N :
        if len(A) < N and len(B) < N and is_connect(A) and is_connect(B):
            global answer
            sum_A, sum_B = 0, 0
            for a in A :
                sum_A += population[a]
            for b in B :
                sum_B += population[b]
            answer = min(answer, abs(sum_A-sum_B))
    else :
        seperate(n+1,A+[n],B)
        seperate(n+1,A,B+[n])


N = int(input())
population = list(map(int, input().split()))
path = [[0]*N for _ in range(N)]

for x in range(N) :
    p = list(map(int, input().split()))
    for i in range(1, p[0]+1) :
        path[x][p[i]-1] = path[p[i]-1][x] = 1

answer = 100*N
seperate(1,[0],[]) 

if answer < 100*N :
    print(answer)
else :
    print(-1)

"""
[반례]
6
2 2 2 2 2 2
1 3
1 4
1 1
1 2
1 6
1 5

[답]
-1
"""
