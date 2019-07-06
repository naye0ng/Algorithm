"""
네트워크
"""

def solution(n, computers):
    answer = 0
    visited = [False]*n

    # 시작값 삽입
    for v in range(n) :
        if visited[v] :
            continue

        queue = []
        queue.append(v)
        while queue :
            q = queue.pop(0)
            for i in range(n) :
                if computers[q][i] == 1 and not visited[i] :
                    queue.append(i)
                    visited[i] = True
        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))