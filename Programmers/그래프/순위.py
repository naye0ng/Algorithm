def solution(n, results):
    G = [[0]*n for _ in range(n)]
    for w,l in results :
        G[w-1][l-1] = 1
        G[l-1][w-1] = -1

    for x in range(n) :
        for y in range(n) :
            if x == y : continue
            if G[x][y] == - 1 :
                visited = [False]*n
                visited[x] = True
                visited[y] = True
                queue = [y]
                while queue :
                    v = queue.pop(0)
                    for i in range(n) :
                        if G[v][i] == -1 and not visited[i]:
                            G[x][i] = -1
                            visited[i] = True
                            queue.append(i)
            if G[x][y] == 1 :
                queue = [y]
                visited = [False]*n
                visited[x] = True
                visited[y] = True
                while queue :
                    v = queue.pop(0)
                    for i in range(n) :
                        if G[v][i] == 1 and not visited[i]:
                            G[x][i] = 1
                            visited[i] = True
                            queue.append(i)
    answer = 0
    for x in range(n) :
        if G[x].count(0)-1 == 1 : answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))