"""
1865.동철이의 일 분배
"""
import sys
sys.stdin = open('input.txt','r')

def work(depth, s) :
    global result
    if depth == len(pn) :
        if result < s :
            result = s
    else :
        for i in range(len(pn)) :
            if visited[i] == 1 :
                continue
            else :
                next = s*(pn[depth][i]/100)
                if next > result :
                    visited[i] = 1
                    work(depth+1, next)
                    visited[i] = 0

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    pn = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N

    result = 0
    work(0,1)
    print('#{} {}'.format(test_case, '%.6f'%(result*100)))
