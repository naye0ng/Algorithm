from itertools import product
import copy

def DFS(s1, s2, cost) :
    global min_cost
    if cost < min_cost :
        if s1 == s2 :
            min_cost = cost
        else :
            for i in range(len(G[s1])) :
                if G[s1][i][1] :
                    G[s1][i][1], temp = 0, G[s1][i][1]
                    DFS(G[s1][i][0], s2, cost+temp)
                    G[s1][i][1] = temp

N, M = map(int, input().split())

G = {}
for key in map(''.join,product(['o','x'], repeat=N)) :
    G[key] = []

for _ in range(M) :
    s1, s2, c = input().split()
    G[s1].append([s2, int(c)])

for _ in range(int(input())) :
    s1, s2 = input().split()
    min_cost = 100*M*M
    DFS(s1, s2, 0)
    if min_cost != 100*M*M :
        print(min_cost)
    else :
        print(-1)