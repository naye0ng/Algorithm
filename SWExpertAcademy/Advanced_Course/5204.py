"""
5204.병합정렬
"""
import sys
sys.stdin = open('input.txt','r')

# b = [0]*1000000
# def mergeSort(a, b, low, high) :
#     if high <= low :
#         return
#     mid = (high+1+low)//2
#     mergeSort(a,b,low,mid-1)
#     mergeSort(a,b,mid,high)
#     if a[mid-1] < a[mid] : return
#     merge(a,b,low,mid-1,high)
#
# def merge(a,b,low,mid,high) :
#     if a[mid] > a[high] :
#         global count
#         count+=1
#
#     for k in range(low,high+1) :
#         b[k] = a[k]
#     i = low
#     j = mid+1
#     for k in range(low,high+1) :
#         if i > mid :
#             a[k] = b[j]
#             j += 1
#         elif j > high :
#             a[k] = b[i]
#             i += 1
#         elif b[j] < b[i] :
#             a[k] = b[j]
#             j += 1
#         else :
#             a[k] = b[i]
#             i += 1

# T = int(input())
# for test_case in range(1,1+T) :
#     N = int(input())
#     a = list(map(int, input().split()))
#     count = 0
#     mergeSort(a,b,0,N-1)
#     print('#{} {} {}'.format(test_case, a[N//2], count))

def mergeSort(m) :
    if len(m) <= 1 :
        return m
    mid = len(m)//2
    left = mergeSort(m[:mid])
    right = mergeSort(m[mid:])
    if left[-1] < right[0] : return right
    return merge(left,right)

def merge(left, right) :
    if left[-1] > right[0] :
        global count
        count+=1
        return left
    return right

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    mergeSort(arr)
    arr.sort()
    print('#{} {} {}'.format(test_case, arr[N//2],count))

