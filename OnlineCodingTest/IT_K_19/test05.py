def solution(stones, k):
    N = len(stones) 
    answer = 200000000*N + 1 
    index = 0
    while index+k <= N :
        # 가장 큰 값의 마지막 위치 찾기
        maxI, maxV = index, stones[index]
        for i in range(index+1,index+k) :
            if stones[i] >= maxV :
                maxV = stones[i]
                maxI = i
        answer = min(answer, maxV)
        index = maxI+1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
# print(solution([5,4,4,1,4,2,4,3,2,2,1],3))
