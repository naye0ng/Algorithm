"""
5202.화물 도크
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    time = [[0,0] for _ in range(N)]
    for n in range(N) :
        time[n][1], time[n][0] = map(int, input().split())
    time.sort()

    result, before, next= 1, 0, 1
    while next < N :
        if time[before][0] <= time[next][1] :
            before = next
            result+=1
        next+=1

    print('#{} {}'.format(test_case, result))