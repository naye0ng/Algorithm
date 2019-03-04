"""
1238.Contact
"""
def contact(start):
    queue = []
    queue.append([0, start])

    depth = 0
    maxitem = 0
    while queue:
        node = queue.pop(0)

        # 깊이가 깊어질때
        if depth < node[0]:
            depth = node[0]
            maxitem = node[1]
        # 깊이가 같은데 현재 노드의 값이 더 클때
        if depth == node[0] and maxitem < node[1]:
            maxitem = node[1]
        for g in G[node[1]]:
            if visitied[g] == 1:
                continue
            queue.append([node[0] + 1, g])
            # 삽입 시에 visitied 체크해줘야 중복으로 가리키는 같은 depth를 피할 수 있음
            visitied[g] = 1
    return maxitem


for test_case in range(1, 11):
    n, start = map(int, input().split())
    path = list(map(int, input().split()))

    visitied = [0 for _ in range(101)]
    G = [[] for _ in range(101)]
    for i in range(0, n, 2):
        G[path[i]] += [path[i + 1]]

    print(f'#{test_case} {contact(start)}')