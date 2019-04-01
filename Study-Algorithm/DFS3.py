def DFS(v) :
    stack = []
    stack.append(v)
    while stack :
        v = stack.pop()
        if not visitied[v] :
            visitied[v] = 1
            print(v)
            for w in range(1, len(G[v])) :
                if G[v][w] and not visitied[w] :
                    stack.append(w)

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visitied = [0] * 8

G = [[0] * 8 for _ in range(8)]
for i in range(0, len(edges), 2):
    G[edges[i]][edges[i + 1]] = 1
    G[edges[i + 1]][edges[i]] = 1

DFS(1)