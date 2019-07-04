"""
쇠막대기 
"""
def solution(arrangement):
    answer = 0
    T = list(arrangement)
    t = 0
    stack = []
    top = 0

    isLaser = False
    while t < len(T) :
        if T[t] == '(' :
            if not isLaser :
                isLaser = True
            stack.append(T[t])
            top += 1
        else :
            stack.pop()
            top -= 1
            if isLaser :
                isLaser = False
                answer += top
            else :
                answer += 1
        t+=1
    return answer

print(solution("()(((()())(())()))(())"))