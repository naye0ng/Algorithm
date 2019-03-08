"""
1959.두 개의 숫자열
"""
import sys
sys.stdin = open('input.txt','r')

def maxSum(I,J, aa,bb) :
    # 길이가 긴 것 : I, aa
    maxS = 0
    for i in range(I-J+1) :
        localS = 0
        for j in range(J) :
            localS += aa[i+j]*bb[j]
        if localS > maxS :
            maxS = localS
    return maxS

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    an = list(map(int, input().split()))
    bn = list(map(int, input().split()))

    if N > M :
        result = maxSum(N,M,an,bn)
    else :
        result = maxSum(M,N,bn,an)

    print('#{} {}'.format(test_case,result))