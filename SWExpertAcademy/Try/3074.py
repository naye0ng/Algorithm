"""
3074.입국심사
"""
import sys
sys.stdin = open('input.txt','r')

def binarySearch(t, best,wast) :
    mid = (best+wast)//2
    people = 0
    for i in range(len(times)) :
        people += mid//times[i]
        if people == t :
            global result
            result = mid
            return
    if people < t :
        binarySearch(t,best,mid-1)
    else :
        binarySearch(t,mid+1,wast)

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    times = [int(input()) for _ in range(N)]
    times.sort()
    best = times[0]*M
    wast = times[-1]*M
    result = 0
    print(times, best, wast)
    binarySearch(M,best,wast)
    print('#{} {}'.format(test_case,result))
