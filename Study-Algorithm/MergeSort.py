"""
병합정렬(Merge Sort) 
"""

def mergeSort(m) :
    if len(m) <=1 :
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right) :
    result = []

    # left, right 한쪽이 0이되면 끝남
    while len(left) > 0 and len(right) > 0 :
        if left[0] <= right[0] :
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))
    
    # left에 원소가 남아있는 경우
    if len(left) > 0 : 
        result.extend(left)
    # right에 원소가 남아있는 경우
    if len(right) > 0 :
        result.extend(right)
    
    return result


m = [69, 10, 30, 2, 16, 8, 31, 22]
print(mergeSort(m))