"""
5189.전자카트
"""
import sys
sys.stdin = open('input.txt','r')

def visit(t,s) :
    if 0 not in visited :
        s+=price[t][0]
        global result
        if result == 0 or result > s :
            result = s
        pass
    else :
        for i in range(len(visited)) :
            if visited[i] == 1 :
                continue
            visited[i] = 1
            visit(i, s+price[t][i])
            visited[i] = 0

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    visited = [0]*N

    visited[0] = 1
    visit(0,0)
    print('#{} {}'.format(test_case,result))
