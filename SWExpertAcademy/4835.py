"""
4835.구간합
"""

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    an = list(map(int,input().split()))

    sums = []
    
    for i in range(0,n-m+1) :
        ss = 0
        for j in range(i,i+m) :
            ss+= an[j]
        sums.append(ss)
    
    print(f'#{test_case} {max(sums)-min(sums)}')



    