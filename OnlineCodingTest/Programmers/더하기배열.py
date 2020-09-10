def get_all_sum(numbers, i, result = 0, depth = 0) :
    if depth == 2 :
        global answer
        answer.append(result)
    else :
        for k in range(i, len(numbers)) :
            get_all_sum(numbers, k+1, result+numbers[k], depth+1)

answer = []
def solution(numbers):
    global answer
    answer = []
    get_all_sum(numbers, 0)
    return sorted(list(set(answer)))

print(solution([2,1,3,4,1]))