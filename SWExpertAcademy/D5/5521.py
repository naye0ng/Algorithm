"""
5521. 상원이의 생일파티
"""
import sys
sys.stdin = open('input.txt','r')

def BFS() :
    queue = [(1, 0)]
    result = 0
    while queue :
        t, depth = queue.pop()
        if depth < 2 :
            for i in range(1,N+1) :
                if arr[t][i] and not visited[i]:
                    queue.append((i,depth+1))
                    visited[i] = 1
                    result+=1
    return result

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M) :
        s, e = map(int, input().split())
        arr[s][e], arr[e][s] = 1, 1
    visited = [0] * (N + 1)
    visited[1] = 1
    print('#{} {}'.format(test_case,BFS()))