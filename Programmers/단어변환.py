"""
단어변환

[설명]
- 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여
  begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
    1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    2. words에 있는 단어로만 변환할 수 있습니다.
- 예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면
  hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.
- 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때,
  최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

[제한]
- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0를 return 합니다.

[입력]
begin	target	words	return
hit	cog	[hot, dot, dog, lot, log, cog]	4
hit	cog	[hot, dot, dog, lot, log]	0
"""
# answer= 0
#
# def DFS(N, visited, words, target, begin) :
#     global answer
#     # 방문한 적이 없는 경우
#     if 1 not in visited :
#         # 타겟에 해당하는 값이 존재한다면
#         try:
#             i = words.index(target)
#             visited[i] = 1
#             next = words[i]
#             answer+=1
#             DFS(N,visited,words,next,begin)
#         except :
#             return 0
#     else :
#         # 하나만 다른 경우 찾기
#         for i in range(N) :
#             # 방문한 적이 없고, 1글자만 다를경우
#             if visited[i] == 0 :
#                 if words[i] == target :
#                     answer+=1
#                     break
#                 # 글자 수 비교
#                 diff = 0
#                 for s in range(len(target)) :
#                     if words[i][s] != target[i][s] :
#                         diff+=1
#                 #글자수 다른게 한 개 뿐이라면
#                 if diff == 1 :
#                     visited[i] =1
#                     next = words[i]
#                     answer+=1
#                     DFS(N,visited,words,next,begin)
#                     visited[i] = 0


def solution(begin, target, words):
    global answer
    N = len(words)
    visited = [0]*N


    return answer





