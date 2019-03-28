"""
5208.전기버스2
"""
import sys
sys.stdin = open('input.txt','r')

def bus(pre, s) :
    global result, N
    if pre == N :
        if result > s:
            result = s
    else :
        for i in range(1,arr[pre]+1) :
            if pre+i > N :
                break
            if s+1 < result :
                bus(pre+i,s+1)

T = int(input())
for test_case in range(1,1+T) :
    arr = list(map(int, input().split()))
    N = arr.pop(0)-1
    result = N
    bus(0,0)
    print('#{} {}'.format(test_case,result-1))