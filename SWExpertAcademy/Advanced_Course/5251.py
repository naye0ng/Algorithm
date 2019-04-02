"""
5251.최소 이동 거리
"""
import sys
sys.stdin = open('input.txt','r')

def dijkstra(s) :
    visited[s] = 1
    D = G[s]

    while 0 in visited :
        mini, w = 0, 0
        for i in range(len(D)) :
            if not visited[i] and (mini == 0 or D[i] < mini) :
                mini = D[i]
                w = i
        visited[w] = 1
        for i in range(len(D)) :
            D[i] = min(D[i], D[w]+G[w][i])
    return D[-1]


T = int(input())
for test_case in range(1,1+T):
    N, E = map(int, input().split())
    G = [[11]*(N+1) for _ in range(N+1)]
    for _ in range(E) :
        s, e, w = map(int, input().split())
        G[s][e] = w
    visited = [0]*(N+1)

    print('#{} {}'.format(test_case, dijkstra(0)))