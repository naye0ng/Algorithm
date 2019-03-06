"""
2805.농작물 수확하기
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    an = [ list(map(int,input().replace(""," ").split())) for _ in range(N)]

    result = 0
    for n in range(N//2) :
        m = n*2+1
        i = N//2
        result += an[n][i]
        result += an[N-1-n][i]
        m-=1
        if m == 0 :
            continue
        for k in range(1,m//2+1) :
            result += an[n][i+k]
            result += an[n][i-k]
            result += an[N-1-n][i+k]
            result += an[N -1-n][i-k]
    # 중간 행 전체 더하기
    result += sum(an[N//2])

    print('#{} {}'.format(test_case, result))