# 그래프의 너비우선탐색
def solution(n, edge):
    G = [[] for _ in range(n)]
    for v, u in edge :
        G[v-1].append(u-1)
        G[u-1].append(v-1)

    visited = [False]*n
    visited[0] = True
    queue = [0]
    answer = 0
    while queue :
        answer = len(queue)
        for _ in range(len(queue)) :
            v = queue.pop(0)
            for u in G[v] :
                if not visited[u] :
                    visited[u] = True
                    queue.append(u)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))