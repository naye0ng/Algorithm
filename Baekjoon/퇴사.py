"""
퇴사
https://www.acmicpc.net/problem/14501
"""
import collections

def DFS(n, start, end, total) :
    global N
    isEnd = True
    for i in range(n+1, N) :
        # 다음 시작일이 끝나는 일보다 커야한다.
        if end < schedule[i][0] :
            DFS(i, schedule[i][0], schedule[i][1], total+schedule[i][2])
            isEnd = False
    if isEnd :
        global result 
        result = max(result, total)
        

N = int(input())
schedule = collections.deque([])
for start in range(1,N+1) :
    end, pay = map(int, input().split())
    if start+end-1 <= N :
        schedule.append([start, start+end-1, pay])

N = len(schedule)
result = 0
for i in range(N) :
    DFS(i, schedule[i][0], schedule[i][1], schedule[i][2])

print(result)