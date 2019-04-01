"""
퀵정렬
"""
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
an = list(map(int,input().split()))
quickSort(0,len(an)-1)
print(an)

# def sort(low, high):
#     if low < high:
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#
# def partition(low, high):
#     pivot = arr[(low + high) // 2]
#     while low <= high:
#         while arr[low] < pivot:
#             low += 1
#         while arr[high] > pivot:
#             high -= 1
#         if low <= high:
#             arr[low], arr[high] = arr[high], arr[low]
#             low, high = low + 1, high - 1
#     return low

# arr = list(map(int,input().split()))
# sort(0,len(arr)-1)
# print(arr)

# 11 45 23 81 28 34
# 3 2 4 6 9 1 8 7 5