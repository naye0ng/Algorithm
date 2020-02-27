"""
회의실배정
https://www.acmicpc.net/problem/1931
"""

N = int(input())
schedule = dict()

break_time = 0
for _ in range(N) :
    start, end = map(int, input().split())
    if end not in schedule :
        schedule[end] = []
    schedule[end].append(start)
    break_time = max(break_time, end)

T, end = 0, 0
result = 0
while T <= break_time :
    # 현재 시간을 기준으로 가장 빨리 끝나는 일정
    choosed = False
    while end <= break_time :
        if end in schedule :
            # 현재 시간보다 같거나 늦게 시작하는 일정이 존재하니?
            schedule[end].sort()
            for start in schedule[end] :
                # 존재한다면, 먼저 시작하는 것부터! 그래야 시작하자마자 끝나는 거 잡을 수 있음
                if start >= T :
                    result += 1
                    schedule[end].pop(0)
                    choosed = True
                    break
        if choosed :
            break
        end += 1
    T = end
print(result) 

"""
11
1 4
3 5
7 7
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""