"""
에산
"""
def binarySearch(budgets, sumL, sumR, ) :
    # if sum(budgets) <= M :
    #     return M
    i = budgets//2
    sumL = sum(budgets[:i])
    sumR = sum(budgets[i:])

    return

def solution(budgets, M):
    answer = 0
    budgets.sort()
    return answer