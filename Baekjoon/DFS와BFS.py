"""
DFS와 BFS
https://www.acmicpc.net/problem/1260
"""
def DFS(v) :
    print(v+1, end=" ") 
    visited[v] = True
    for i in range(N) :
        if graph[v][i] and not visited[i] :
            DFS(i)
def BFS(v) :
    visited = [False]*N
    queue = []
    queue.append(v)

    while queue :
        v = queue.pop(0)
        if not visited[v] :
            print(v+1, end=" ") 
            visited[v] = True

        for i in range(N) :
            if graph[v][i] and not visited[i] :
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[0]*N for _ in range(N)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a-1][b-1], graph[b-1][a-1] = 1, 1

visited = [False]*N
DFS(V-1)
print()
BFS(V-1)