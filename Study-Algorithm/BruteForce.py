def BruteForce(t, p) :
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    while j < M and i < N :
        # print(1,i,j)
        if t[i] != p[j] :
            i = i - j
            j = -1
        # print(2,i,j)    
        i += 1
        j += 1
    # print(i,j)
    if j == M : return i - M
    else: return i


T = "dadddddgdsasdfesdfkasdf"
P = "ddddd"
print(T[ BruteForce(T, P):] )