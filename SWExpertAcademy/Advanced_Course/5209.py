"""
5209.최소 생산 비용
"""
import sys
sys.stdin = open('input.txt','r')

def doit(p, s) :
    global result, N
    if 0 not in visited :
        if result == 0 or result > s :
            result = s
    else :
        for i in range(N) :
            if visited[i] :
                continue
            next = s+price[p][i]
            if result == 0 or next < result :
                visited[i] =1
                doit(p+1,next)
                visited[i] =0

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    price = [ list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    doit(0,0)
    print('#{} {}'.format(test_case,result))
