"""
5207.이진탐색
"""
import sys
sys.stdin = open('input.txt','r')

def binarySearch(arr, t, pre):
    # 일치하는 값이 없는 경우
    if len(arr) == 0 :
        return
    l = 0
    r = len(arr)-1
    m = (l + r) // 2
    if arr[m] == t :
        global result
        result+=1
    elif arr[m] < t and pre != 1 :
        binarySearch(arr[m+1:],t,1)
    elif arr[m] > t and pre != -1 :
        binarySearch(arr[:m],t,-1)
    return

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    result = 0
    for t in list(map(int, input().split())) :
        binarySearch(A,t,0)

    print('#{} {}'.format(test_case, result))