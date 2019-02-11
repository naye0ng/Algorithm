"""
4864.문자열 비교
"""
def findString(t, p) :
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    while j < M and i < N :
        if t[i] != p[j] :
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M : 
        return 1
    else: 
        return 0

T = int(input())
for test_case in range(1, T + 1):
    pn = input().replace(""," ").split()
    an = input().replace(""," ").split()

    print(f'#{test_case} {findString(an,pn)}')

    
