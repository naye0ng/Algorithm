"""
가장 먼 노드 - BFS
"""
def solution(n, edge):
    global answer
    answer = [0]*(n+1)

    G = [ [] for _ in range(n+1) ]
    for i, j in edge :
        G[i].append(j)
        G[j].append(i)

    queue = []
    visited = [False]*len(G)

    queue.append([1,0])
    while queue :
        q = queue.pop(0)
        if not visited[q[0]] :
            visited[q[0]] = True
            answer[q[0]] = q[1]
            for g in G[q[0]] :
                if not visited[g] :
                    queue.append([g,q[1]+1])
    return answer.count(max(answer))

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])