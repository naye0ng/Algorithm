"""
병합정렬(Merge Sort) 
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    if left[-1] < right[0]: return left + right
    return merge(left, right)

def merge(left, right):
    result = []
    # 한쪽이 0이 되면 비교는 끝내고, 남은 부분을 붙여주기만 하면 된다.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    elif len(right) > 0:
        result.extend(right)
    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(mergeSort(arr))