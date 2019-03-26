"""
실패율
"""
def solution(N, stages):
    contact = [0]*(N+2)
    fail = [0]*N
    for s in stages :
        contact[s] += 1
    l = len(stages)
    p = 0
    for i in range(1,N+1) :
        if l-p == 0 :
            fail[i - 1] = [1, i]
        else :
            fail[i-1] = [1-contact[i]/(l-p),i]
            p += contact[i]
    fail.sort()
    result =[]
    for f in fail :
        result.append(f[1])
    return result

print(solution(5,[2, 1, 2, 2, 4, 3, 3]))