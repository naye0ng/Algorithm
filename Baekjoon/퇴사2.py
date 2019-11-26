"""
퇴사2
https://www.acmicpc.net/problem/15486
"""
import collections

N = int(input())
schedule = collections.deque([])
for start in range(1, N+1) :
    end, pay = map(int, input().split())
    if start+end-1 <= N :
        schedule.appendleft([start, start+end-1, pay])

N = len(schedule)
visited = [False]*N
result = 0
for i in range(N) :
    # 이전에 호출된 적이 있다면, 이전 것이 더 크다.
    if visited[i] == False :
        # i번째 값을 시작으로 queue를 구성한다.
        queue = collections.deque([schedule[i]])
        visited[i] = True
        while queue :
            start, end, pay = queue.popleft()
            result = max(result, pay)
            for n in range(i+1,N) :
                if schedule[n][1] < start :
                    visited[n] = True
                    queue.append([schedule[n][0],schedule[n][1], pay+schedule[n][2]])

print(result)
