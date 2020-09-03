'''
타임머신
https://www.acmicpc.net/problem/11657
'''
import copy

# 사이클도 판별해야함 : N번 돌린다.
def Bellman_Ford(before, depth) :
    after = copy.deepcopy(before)
    for v in range(V) :
        if before[v] == INF : continue
        for u in range(V) :
            if G[v][u] == INF : continue
            after[u] = min(after[u], before[v]+G[v][u])
    if depth == 0 :
        # 음의 싸이클체크 : N-1번과 N번 사이에 달라진 것이 있다면, 싸이클이 존재
        for x in range(V) :
            if before[x] == after[x] : continue
            return print(-1)

        for x in range(1, V) :
            if after[x] == INF : print(-1)
            else : print(after[x])        
        return 
    else :
        Bellman_Ford(after, depth-1)


V, E = map(int, input().split())
INF = V*V*10000

G = [[INF]*V for _ in range(V)]
for _ in range(E) :
    v, u, w = map(int, input().split())
    G[v-1][u-1] = min(G[v-1][u-1], w)

arr = [INF]*V
arr[0] = 0

Bellman_Ford(arr, V)


'''
3 3
1 2 3
2 1 -1000
2 1 5

'''