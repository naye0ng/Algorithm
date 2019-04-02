"""
5249.최소신장트리
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,1+T) :
    V, E = map(int, input().split())
    root = [i for i in range(V+1)]
    edge = [[0]*3 for _ in range(E)]
    for i in range(E) :
        n1, n2, w = map(int, input().split())
        edge[i] = [w,n1,n2]
    edge.sort()
    result = 0
    for e in edge :
        w, n1, n2 = e[0], e[1], e[2]
        # 사이클
        if root[n1] == root[n2] : continue

        result += w
        if root[n1] > root[n2] : root[n1], root[n2] = root[n2], root[n1]
        next = root[n2]
        for i in range(1,V+1) :
            if root[i] == next :
                root[i] = root[n1]

    print('#{} {}'.format(test_case, result))