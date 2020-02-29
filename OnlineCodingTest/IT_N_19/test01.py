def solution(prices):
    N = len(prices)
    answer = [0]*N
    stack = [[prices[0],0]]
    for i in range(1,N) :
        while True :
            if stack[-1][0] <= prices[i] :
                stack.append([prices[i],i])
                break
            else :
                s, j = stack.pop()
                answer[j] = i-j
        print(answer)
    return answer

solution([1, 2, 3, 2, 3])