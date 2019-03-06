"""
2005.파스칼의 삼각형
"""
T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    triangle = []

    print('#{}'.format(test_case))
    for n in range(1,N+1) :
        sub = []
        for i in range(n) :
            if i == 0 or i == n-1 :
                sub.append(1)
            else :
                sub.append(triangle[n-2][i-1]+triangle[n-2][i])
        triangle.append(sub)
        print(" ".join( map(str, sub)))
