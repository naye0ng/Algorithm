def solution(strs):
    # 접두사 후보 찾기
    N, answer = 1001, ""
    for s in strs :
        if len(s) < N :
            N, answer = len(s), s

    for i in range(N) :
        for j in range(len(strs)) :
            if strs[j][i] != answer[i] :
                return answer[:i]
    return answer