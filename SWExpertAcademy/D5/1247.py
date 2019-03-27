"""
최적경로
"""
import sys
sys.stdin = open('input.txt','r')

def visit(pre, s) :
    global result
    if result == 0 or s < result :
        if 0 not in visited :
            s += abs(path[pre][0]-end[0])+abs(path[pre][1]-end[1])
            if result == 0 or result > s :
                result = s
        else :
            for i in range(1,len(visited)) :
                if visited[i] == 0 :
                    visited[i] = 1
                    s2 = abs(path[i][0] - path[pre][0]) + abs(path[i][1] - path[pre][1])
                    visit(i,s+s2)
                    visited[i] = 0

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    temp = list(map(int, input().split()))
    path = [[temp[i],temp[i+1]] for i in range(0,len(temp),2)]
    end = path.pop(1)
    visited = [0]*len(path)

    result = 0
    visited[0] = 1
    visit(0, 0)
    print('#{} {}'.format(test_case, result))
