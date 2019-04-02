"""
5248.그룹 나누기
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))

    root = [i for i in range(N+1)]
    for i in range(M) :
        t1, t2 = edges[i*2], edges[i*2+1]
        if t1 > t2 :
            t1, t2 = t2, t1
        t = root[t2]
        for k in range(1,N+1) :
            if root[k] == t :
                root[k] = root[t1]
    result = 0
    for i in range(1,N+1) :
        if root[i] == i :
            result+=1
    print('#{} {}'.format(test_case, result))