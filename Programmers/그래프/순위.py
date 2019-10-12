import collections

# n이 이긴 애들의 갯수
def win(n, m) :
    global player
    visited = [0]*n
    queue = collections.deque(player[m][0])
    num = len(queue)
    for i in range(num) :
        visited[queue[i]] = True
    while queue :
        q = queue.popleft()
        for k in player[q][0] :
            if visited[k] == False :
                visited[k] = True
                queue.append(k)
                num += 1
                player[m][0].add(k)
    return num

def lose(n, m) :
    global player
    visited = [0]*n
    queue = collections.deque(player[m][1])
    num = len(queue)
    for i in range(num) :
        visited[queue[i]] = True
    while queue :
        q = queue.popleft()
        for k in player[q][1] :
            if visited[k] == False :
                visited[k] = True
                queue.append(k)
                num += 1
                player[m][1].add(k)
    return num

player = []
def solution(n, results):
    global player
    player = [[set() for i in range(2)] for _ in range(n)]
    # 노드 초기화
    for result in results :
        winner, loser = result
        player[winner-1][0].add(loser-1)
        player[loser-1][1].add(winner-1)
    
    answer = 0
    for i in range(n) :
        if win(n,i) + lose(n,i) == n-1 :
            answer += 1
    
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))