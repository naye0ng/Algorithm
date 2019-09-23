"""
에산
"""
# 이분탐색으로 찾기
def solution(budgets, M):
    budgets.sort()
    N = len(budgets)
    l, r = 0, N-1
    # 전체 다 가능한지 체크
    if sum(budgets) <= M :
        return budgets[-1]
    # 전체 다 불가능한지 체크
    if budgets[0]*N > M :
        return M//N
    visited = [False]*N
    while True :
        m = (l+r)//2
        if visited[m] == False :
            visited[m] = True
            if sum(budgets[:m+1])+budgets[m]*(N-(m+1)) <= M :
                l = m
            else :
                r = m
        else : break
    # 인덱스가 l까지만 가능
    return(M-sum(budgets[:l+1]))//(N-(l+1))

print(solution([9, 8, 5, 6, 7],5))