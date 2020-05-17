"""
구명보트
https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
"""
def pick(N, limit, people, n, boat) :
    if n == N :
        global answer
        answer = min(answer, boat)
    else :
        for i in range(N) :
            # 선택되지 않은 것과 같이 선택될 수 있는 값 찾기
            if not picked[i] :
                picked[i] = True
                not_together = True
                for j in range(i+1,N) :
                    if not picked[j] and people[i]+people[j] <= limit :
                        picked[j] = True
                        not_together = False
                        pick(N, limit, people, n+2, boat+1)
                        picked[j] = False
                if not_together :
                    pick(N, limit, people, n+1, boat+1)
                picked[i] = False

answer = 0
picked = []
def solution(people, limit):
    global picked, answer
    N = len(people)
    picked = [False]*N
    answer = N
    pick(N, limit, people, 0, 0)

    return answer