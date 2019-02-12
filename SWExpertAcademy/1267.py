"""
1267.작업순서
"""
def check(s) :
    if 1 in G[s] and visitied[s] == 0:
        check(G[s].index(1))
    elif 2 in G[s] :
        parents = G[s].index(2)
        if visitied[parents] == 0 :
            visitied[s] = 1
            print(s+1,end=' ')
            # 자기 자신 고립
            for i in range(len(G)):
                if G[i][s] :
                    G[i][s] = 0
            check(parents)
    else :
        visitied[s] = 1
        print(s+1,end=' ')
        # 자기 자신 고립
        for i in range(len(G)):
            if G[i][s] :
                G[i][s] = 0
        if  0 in visitied :
            check(visitied.index(0))


for test_case in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))

    G = [[0]*v for _ in range(v)]
    visitied = [0]*v

    for i in range(0, len(edges),2) :
        G[edges[i]-1][edges[i+1]-1] = 2
        G[edges[i+1]-1][edges[i]-1] = 1

    print(f'#{test_case}', end=' ')
    check(0)
    print()
