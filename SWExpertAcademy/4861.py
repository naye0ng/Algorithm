"""
4861.회문
"""
# import sys
# sys.stdin = open('input.txt', 'r')

def searchcircle(an,n,m) :
    for i in range(n) :
        for j in range(n-m+1) :
            ch1, ch2 = 0,0
            for k in range(m//2) :
                if an[i][j+k] == an[i][j+m-1-k] :
                    ch1 += 1
                if an[j + k][i] == an[j + m - 1 - k][i]:
                    ch2 += 1
            if ch1 == m//2 :
                return "".join(an[i][j:j+m])
            elif ch2 == m//2 :
                result = ""
                for h in range(m) :
                    result+= an[j+h][i]
                return result

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    an = [input().replace("", " ").split() for i in range(n)]

    print(f'#{test_case} {searchcircle(an,n,m)}')



    

