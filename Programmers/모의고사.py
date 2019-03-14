"""
모의고사
"""
def solution(answers):
    # 길이 5, 8, 10
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s1, s2, s3 = 0, 0, 0
    for i in range(len(answers)) :
        s1 += people[0][i % 5] == answers[i]
        s2 += people[1][i % 8] == answers[i]
        s3 += people[2][i % 10] == answers[i]

    answer = []
    maxV = max(s1,s2,s3)
    if s1 == maxV :
        answer.append(1)
    if s2 == maxV :
        answer.append(2)
    if s3 == maxV :
        answer.append(3)

    return answer