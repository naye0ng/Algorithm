'''
플로이드
https://www.acmicpc.net/problem/11404
'''
def convert_inf(i) :
    if i == INF : return 0
    return i

V = int(input())
E = int(input())

INF = V*V*100000

G = [[INF]*V for _ in range(V)]
for x in range(V) :
    G[x][x] = 0

for _ in range(E) :
    v, u, w = map(int, input().split())
    # [해결] 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    G[v-1][u-1] = min(G[v-1][u-1], w)

'''
시간복잡도 : N^3
'''
for k in range(V) :
    for x in range(V) :
        if k == x : continue
        for y in range(V) :
            if k == y : continue
            if G[x][y] > G[x][k]+G[k][y] :
                G[x][y] = G[x][k]+G[k][y]

for x in range(V) :
    print(" ".join(map(lambda i: str(convert_inf(i)), G[x])))