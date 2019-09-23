"""
입국심사
"""
def match(times,t) :
    n = 0
    isMatch = False
    for time in times :
        n += t//time
        if t%time == 0 :
            isMatch = True
    return n, isMatch

def solution(n, times):
    t = min(times)
    l, r = t, t*n
    while True :
        mid = (l+r)//2
        m, isMatch = match(times, mid)
        if m == n :
            # 같고 다름
            if isMatch :
                return mid
            else :
                r == mid
        elif m < n :
            l = mid
        else :
            r = mid
print(solution(6,[7,10]))