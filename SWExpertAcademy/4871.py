"""
4871.그래프 경로
1
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9


"""
def check(s,g) :
    if g == s :
        global result
        result = 1
        return
    for i in range(len(G[g-1])):
        if G[g-1][i] == 1:
            # 사이클 제거
            G[g-1][i] = 0
            check(s,i+1)


T = int(input())
for test_case in range(1, T + 1):
 
    v, e = map(int, input().split())
    # 간선리스트로 구해보자
    edges = [ list(map(int,input().split())) for _ in range(e)]

    G = [[0] * v for _ in range(v) ]
    # 거꾸로 써야 도착노드부터 올라기 편함
    for i in range(len(edges)) :
        G[edges[i][1]-1][edges[i][0]-1] = 1

    s, g = map(int, input().split())

    # for i in G :
    #     print(i) 
    result = 0
    check(s,g)
    print(f'#{test_case} {result}')

