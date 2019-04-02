"""
5247.연산
"""
import sys
from collections import deque
sys.stdin = open('input.txt','r')

def isWall(p) :
    if p < 0 or p > 1000000 :
        return True
    if visited[p] == 1 :
        return True
    return False

def module(s, t) :
    queue = deque()
    queue.append([s,0])
    n = 0
    while n < 1000000 :
        sn = queue.popleft()
        s = sn[0]
        n = sn[1]
        if s == t :
            break
        if not isWall(s-1) :
            visited[s-1] = 1
            queue.append([s-1,n+1])
        if not isWall(s+1):
            visited[s+1] = 1
            queue.append([s+1,n+1])
        if not isWall(s*2):
            visited[s*2] = 1
            queue.append([s*2, n+1])
        if not isWall(s-10):
            visited[s-10] = 1
            queue.append([s-10,n+1])
    return n

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    visited = [0 for i in range(1000001)]

    print('#{} {}'.format(test_case, module(N,M)))