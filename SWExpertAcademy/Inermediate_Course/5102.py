"""
5102.노드의 거리
"""
def BFS(start, end) :
    queue = []
    # 시작점부터 탐색 시작
    queue.append([0,start])

    while queue :
        node = queue.pop(0)
        visitied[node[1]] = 1
        #  node[1]에 해당하는 값의 방문한 적 없는 하위 경로 검사
        for g in G[node[1]] :
            if visitied[g] :
                continue
            if g == end :
                return node[0]+1
            queue.append([node[0]+1,g])
    return 0

T = int(input())
for test_case in range(1,T+1) :
    v, e = map(int, input().split())
    edge = [map(int, input().split()) for _ in range(e) ]
    start, end = map(int, input().split())

    visitied = [0 for _ in range(v+1)]
    G = [[] for _ in range(v+1)]

    for x, y in edge :
        G[x] += [y]
        G[y] += [x]

    print(f'#{test_case} {BFS(start, end)}')