"""
완주하지 못한 선수
"""
# def solution(participant, completion):
#     # answer = ''
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)) :
#         if participant[i] != completion[i] :
#             return participant[i]
#     return participant[-1]


# 다른 사람 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(["leo", "kiki","kiki", "eden"], ["eden", "kiki","leo"]))
