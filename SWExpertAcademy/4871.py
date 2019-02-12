"""
4871.그래프 경로
"""
def check(s,g) :
    if g==s :
        return 1
    elif 1 not in G[g] :
        return 0
    c = 0
    for i in range(0,len(G[g])):
        if G[g][i] == 1:
            c += check(s,i)
    return c

T = int(input())
for test_case in range(1, T + 1):
 
    v, e = map(int, input().split())
    edges = [ list(map(int,input().split())) for _ in range(e)]

    G = [[0] * v for _ in range(v) ]
    # 거꾸로 써야 도착노드부터 올라기 편함
    for i in range(0, len(edges)) :
        G[edges[i][1]-1][edges[i][0]-1] = 1


    # for i in range(len(G)) :
    #     print(i+1, G[i])

    s, g = map(int, input().split())
    
    print(f'#{test_case} {check(s-1,g-1)}')