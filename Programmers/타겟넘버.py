"""
타겟 넘버

[설명]
- n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
- 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

[입력]
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""

def makeEqual(numbers,t,i, target) :
    global N
    if i == N:
        # 전부다 방문을 했다면
        if t == target :
            global answer
            answer+=1
    else :
        # 다음값 더하기
        makeEqual(numbers,t+numbers[i],i+1,target)
        # 다음값 빼기
        makeEqual(numbers,t-numbers[i],i+1,target)

def solution(numbers, target):
    global N, answer
    N = len(numbers)
    answer = 0

    makeEqual(numbers,numbers[0],1,target)
    makeEqual(numbers,-1*(numbers[0]),1,target)

    return answer

# 답은 5가 나와야 한다.
print(solution([1, 1, 1, 1, 1],3))