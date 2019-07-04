"""
가장 먼 노드
"""
def maxNode(G, visited, v,  num) :
    for g in G[v] :
        if not visited[g] and answer[v] == 0:
            visited[g] = True
            maxNode(G, visited, g, num+1)
            visited[g] = False
        else :
            # 더 이상 갈 곳이 없다면 최대
            answer[v] = num


def solution(n, edge):
    global answer
    answer = [0]*(n+1)

    G = [ [] for _ in range(n+1) ]
    for i, j in edge :
        G[i].append(j)
        G[j].append(i)

    visited = [False]*(n+1)
    visited[1] = True
    maxNode(G, visited,1,0)
    print(answer)

    return answer.count(max(answer))

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])