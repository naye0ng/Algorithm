"""
여행경로

[설명]
- 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
- 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
  방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

[제한]
- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
"""
answer, N = [], 0
def makePath(i,an,target,visited) :
    if i == N+2 :
        global answer
        answer = an
        return 1
    else :
        nextTargets = []
        for i in range(N):


def solution(tickets):
    global answer, N
    # 인천공항 찾기
    N = len(tickets)
    ICN = []
    for i in range(N) :
        if tickets[i][0] == "ICN" :
            ICN.append([tickets[i][1],i])
    ICN.sort()
    for k in range(len(ICN)):
        # 함수 호출
        an = [0]*(N+1)
        an[0] = "ICN"
        visited = [0]*N
        visited[ICN[k][0]] =1
        makePath(1, an,ICN[k][0])
        if len(answer) > 0 :
            break






    return answer