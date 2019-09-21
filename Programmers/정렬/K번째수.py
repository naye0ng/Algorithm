def solution(array, commands):
    answer = []
    i = 0
    while i < len(commands) :
        q = commands[i]
        arr = array[q[0]-1:q[1]]
        arr.sort()
        answer.append(arr[q[2]-1])
        i+= 1
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))



"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""