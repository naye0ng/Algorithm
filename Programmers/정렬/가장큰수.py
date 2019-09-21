def mergeSort(arr) :
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def merge(left, right) :
    result = []
    while len(left) > 0 and len(right) > 0 :
        if left[0]+right[0] > right[0]+left[0] :
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))
    if len(left) > 0 :
        result.extend(left)
    elif len(right) > 0 :
        result.extend(right)
    return result

def solution(numbers):        
    return str(int("".join(mergeSort(list(map(str,numbers))))))
    

print(solution([3, 30, 34, 5, 9]))