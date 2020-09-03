'''
최단경로
https://www.acmicpc.net/problem/1753
'''
import heapq

V, E = map(int, input().split())
K = int(input())-1
INF = 10*V*V

'''
# [그래프 구현 1] 인접행렬
# 20000*20000 크기의 배열은 메모리 초과가 발생할 수 있다.
G = [[INF]*V for _ in range(V)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    G[u-1][v-1] = w
'''

# [그래프 구현 2] 인접리스트
G = [[] for _ in range(V)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    G[u-1].append([v-1, w])

P = [INF]*V
P[K] = 0

'''
# [다익스트라 구현 1] 그리디
# 시간복잡도 N^2 : 시간초과
visited = [False]*V
while K >= 0 :
    visited[K] = True
    for u in range(V)  :
        if u == K or u not in G[K] : continue
        P[u] = min(P[u], P[K]+G[K][u])
    
    K, minW = -1, INF
    for v in range(V) :
        if visited[v] : continue
        if P[v] < minW :
            K, minW = v, P[v]
'''


# [다익스트라 구현 2] 우선순위 큐
Q = []
heapq.heappush(Q, [0, K])
for v in range(V) :
    if v == K : continue
    heapq.heappush(Q, [INF, v])

while Q :
    dist, v = heapq.heappop(Q)
    if P[v] == dist :
        # [핵심] 모든 점의 연결을 볼 필요 없음, v에 연결된 점만 확인
        for u, w in G[v] :
            w += dist
            if P[u] > w :
                P[u] = w
                heapq.heappush(Q, [w, u])

for path in P :
    if path == INF : path = 'INF'
    print(path)
