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
answer,Tickets, N = [],[], 0

def makePath(index,an,target,visited) :
    # 끝까지가는 경로가 존재한다면 정답에 넣기
    if index == N :
        an[index] = target
        global answer
        answer = an
        return
    else :
        # for 문을 돌면서 다음타겟들을 돌린다.
        nextTargets = []
        for i in range(N):
            #방문한 적없는 경로이고, 타겟과 같다면 넣는다.
            if visited[i] == 0 and Tickets[i][0] == target :
                nextTargets.append([Tickets[i][1],i])
        nextTargets.sort()
        for k in range(len(nextTargets)) :
            an[index] = target
            visited[nextTargets[k][1]] = 1
            makePath(index+1,an,nextTargets[k][0],visited)
            if len(answer) > 0 :
                break
            visited[nextTargets[k][1]] = 0

def solution(tickets):
    global answer,Tickets, N
    Tickets = tickets
    # 인천공항 찾기
    N = len(tickets)
    ICN = []
    for i in range(N) :
        if tickets[i][0] == "ICN" :
            ICN.append([tickets[i][1],i])
    # 시작지점을 찾을건데, 알파벳의 오름차순으로 정렬한 순서대로 함수 호출, [이동할 곳, 해당경로의 인덱스]형태로 저장됨
    ICN.sort()
    for k in range(len(ICN)):
        # an은 경로저장 배열, 인천공항에서부터 시작
        an = [0]*(N+1)
        an[0] = "ICN"
        # 방문한 경로 저장
        visited = [0]*N
        visited[ICN[k][1]] = 1

        makePath(1, an,ICN[k][0],visited)
        if len(answer) > 0 :
            break
        visited[ICN[k][1]] = 0

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


"""
다른사람의 풀이 분석해보기
"""
candidates = []
def visit(start, graph, visited, cnt, route):
    global candidates
    if cnt == len(graph):
        candidates.append(route.split(" "))
    else:
        for i in range(len(graph)):
            if visited[i] == 0 and graph[i][0] == start:
                go = []
                for j in range(len(visited)):
                    go.append(visited[j])
                go[i] = 1
                visit(graph[i][1], graph, go, cnt+1, route+" "+graph[i][1])

def solution(tickets):
    tickets.sort()
    visited = [0] * len(tickets)
    visit("ICN", tickets, visited, 0, "ICN")
    return candidates[0]