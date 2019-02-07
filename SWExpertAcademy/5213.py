"""
5213.진수의 홀수 약수

- f(x)는 x의 약수 중에서 홀수인 것들의 합이라고 하자.
- 두 자연수 L과 R 사이의 모든 자연수 x에 대해서 f(x)의 총 합을 계산하라.
"""
import math

# 소수에서 에라토스테네스의 체처럼, 홀수 약수의 누적합을 가진 배열을 만들고 시작하자
def odd(x) :
    odds = [i if i%2 else 0 for i in range(1,x+1)]
    oddsum = [ 0 for i in range(x)]

    for i in range(len(odds)) :
        if odds[i] == 0 :
            # 누적
            oddsum[i] += oddsum[i-1]
            continue
        for j in range(i,len(odds),odds[i]) :
            oddsum[j]+=odds[i]
        # 누적
        if i == 0 : 
            continue
        oddsum[i] += oddsum[i-1]

    return oddsum

sums = odd(1000000)

T = int(input())
for test_case in range(1, T + 1):
    l, r = map(int,input().split())
    if l == 1 :
        print(f'#{test_case} {sums[r-1]}')
    else :
        print(f'#{test_case} {sums[r-1]-sums[l-2]}')




