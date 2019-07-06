"""
여행경로
"""

def travel(tickets,answer,visited,before, n) :
    if answer[-1] != 0 :
        return True
    else :
        isPossible = False
        for t in range(len(tickets)) :
            if not visited[t] and tickets[t][0] == before :
                visited[t] = True
                answer[n+1] = tickets[t][1]
                isPossible = travel(tickets,answer,visited,tickets[t][1],n+1)
                if isPossible :
                    return isPossible
                answer[n+1] = 0
                visited[t] = False
        return isPossible

def solution(tickets) :
    tickets.sort()
    answer = [0]*(len(tickets)+1)
    answer[0] = 'ICN'
    visited = [False]*len(tickets)

    # 인천공항에서 출발
    i = 0
    isPossible = False
    while i < len(tickets) :
        if tickets[i][0] == 'ICN' :
            visited[i] = True
            answer[1] = tickets[i][1]
            isPossible = travel(tickets,answer,visited,tickets[i][1],1)
            if isPossible :
                break
            answer[1] = 0
            visited[i] = False
        i += 1
    return answer

print(solution(	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))