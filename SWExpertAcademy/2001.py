"""
2001.파리퇴치
"""
t = int(input())

for test_case in range(1,t+1) :
    n, m = map(int, input().split())
    an = [ list(map(int,input().split())) for j in range(n)]


    maxAn = 0 
    for i in range(n-m+1):
        for j in range(n-m+1):
            sumAn = 0
            # 합 구하기... 
            for y in range(0,m) :
                for x in range(0,m) :
                    sumAn += an[j+x][i+y]
            
            if maxAn < sumAn :
                maxAn = sumAn

    print(f'#{test_case} {maxAn}')
