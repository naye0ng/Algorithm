"""
에산
"""
def solution(budgets, M):
    N = len(budgets)
    budgets.sort()
    isPossible = 0
    # 배정 가능한 갯수 찾기
    while isPossible < N:
        if sum(budgets[:isPossible+1])+budgets[isPossible]*(N-(isPossible+1)) <= M : isPossible += 1
        else : break
    
    return (M-sum(budgets[:isPossible]))//(N-isPossible) if isPossible < N else budgets[-1]
        
print(solution([120, 110, 140, 150],485))