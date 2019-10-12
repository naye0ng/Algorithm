def perm(N, k, before, result) :
    if N == k :
        global answer
        answer = max(answer, result)
    else :
        for i in range(N) :
            if visited[i] == False :
                visited[i] = True
                perm(N, k+1, target[i], result+abs(before-target[i]))
                visited[i] = False

answer, visited, target = 0, [], []
def solution(v):
    global answer, visited, target
    answer = 0
    N = len(v)
    target = v
    visited = [False]*N

    for i in range(N) :
        visited[i] = True
        perm(N, 1, target[i], 0)
        visited[i] = False

    return answer