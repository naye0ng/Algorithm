"""
6190.정곤이의 단조 증가하는 수
"""
import sys
sys.stdin = open('input.txt','r')

def isIncrease(t) :
    while t :
        a1 = t%10
        t = t//10
        a2 = t%10
        if a1 < a2 : return False
    return True

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    an = list(map(int, input().split()))

    # 단조증가 후보 찾기
    maxValue = -1
    for n in range(N-1) :
        for k in range(n+1,N) :
            t = an[n]*an[k]
            if isIncrease(t):
                if maxValue < t :
                    maxValue = t

    print('#{} {}'.format(test_case,maxValue))