"""
4843.특별한 정렬
"""

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    an = list(map(int,input().split()))
    bn = []


    #an정렬
    for i in range(n-1) :
        max = an[i]
        k = i
        for j in range(i+1,n) :
            if max < an[j] :
                max = an[j]
                k = j
        if k != i :
            an[k] = an[i]
            an[i] = max
    
    for i in range(n//2):
        bn.append(an[i])
        bn.append(an[n-1-i])

    if n%2 :
        bn.append(an[n//2])
    
    print(f'#{test_case} {" ".join(map(str,bn[:10]))}')
