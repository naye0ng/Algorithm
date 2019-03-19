"""
소수찾기

- 조합 라이브러리 설명
https://ourcstory.tistory.com/414
"""
# 소수 배열을 먼저 만들고 시작한다.
# 7자리 0~9까지의 수가 들어오므로 0 ~ 9999999까지 가능
decimal = [i for i in range(10000000)]
decimal[1] = 0
for i in range(2, len(decimal)) :
    if decimal[i] == 0 :
        continue
    else :
        for k in range(i*2,len(decimal),i) :
            if decimal[k] == 0 :
                continue
            decimal[k] = 0

answer = 0

def DFS(t,visited,numbers) :
    # 들어오는 숫자가 소수인지 체크
    if decimal[t] != 0 :
        global answer
        answer += 1
        # 추가 카운팅 방지
        decimal[t] = 0
    # 모두 방문 했으면
    if 0 not in visited :
        return
    else :
        for i in range(len(numbers)) :
            if visited[i] == 1 :
                continue

            visited[i] = 1
            DFS(t*10+numbers[i],visited,numbers)
            visited[i] = 0

def solution(numbers):
    numbers = list(map(int,numbers.replace(""," ").split()))
    N = len(numbers)
    visited =[0]*N
    for i in range(N) :
        visited[i] = 1
        DFS(numbers[i],visited,numbers)
        visited[i] = 0
    global answer
    return answer

print(solution("011"))
