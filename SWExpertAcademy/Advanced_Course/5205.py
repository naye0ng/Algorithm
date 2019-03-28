"""
5205.퀵정렬
"""
import sys
sys.stdin = open('input.txt','r')

def quickSort(l,r) :
    if l < r :
        mid = partition(l,r)
        quickSort(l,mid-1)
        quickSort(mid,r)

def partition(l,r) :
    pivot = an[(l+r)//2]
    while l <= r :
        while an[l] < pivot : l+=1
        while an[r] > pivot : r-=1
        if l <= r :
            an[l], an[r] = an[r], an[l]
            l += 1
            r -= 1
    return l

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    an = list(map(int, input().split()))
    quickSort(0,len(an)-1)

    print('#{} {}'.format(test_case,an[N//2]))
