"""
케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389
"""
def BFS(x) :
    queue = []
    queue.append([x,0])
    visited = [False]*N

    while queue :
        y, num = queue.pop(0)

        visited[y] = True
        if G2[x][y] == 0 :
            G2[x][y] = num

        for i in range(N) :
            if G[y][i] != 0 and not visited[i]:
                queue.append([i,num+G[y][i]])


N, M = map(int, input().split())
G = [[0]*N for _ in range(N)]
G2 = [[0]*N for _ in range(N)]

for _ in range(M) :
    a, b = map(int, input().split())
    G[a-1][b-1], G[b-1][a-1] = 1, 1
    G2[a-1][b-1], G2[b-1][a-1] = 1, 1


for n in range(N) :
    BFS(n)

node, min_kevin = 1, sum(G2[0])
for n in range(1,N) :
    kevin = sum(G2[n])
    if kevin < min_kevin :
        min_kevin = kevin
        node = n+1
print(node)
    

"""
3 3
1 2
2 3
1 3
"""