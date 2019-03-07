"""
2606.바이러스
"""
def virus(t) :
    Queue = []
    Queue.append(t)
    visited[t - 1] = 1

    num = 0
    while len(Queue) :
        p = Queue.pop()
        for i in range(1,N+1) :
            if G[p][i] == 1 and visited[i-1] == 0 :
                Queue.append(i)
                visited[i - 1] = 1
                num+=1
    return num

N = int(input())
M = int(input())

G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    x, y = map(int, input().split())
    G[x][y] = 1
    G[y][x] = 1

visited = [0]*N
print(virus(1))


