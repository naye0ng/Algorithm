"""
1946.간단한 압축 풀기
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    an = [input().split() for _ in range(N)]

    blank = []
    for a in an :
        blank+= a[0]*int(a[1])

    # 출력
    print('#{}'.format(test_case))
    for i in range(1,len(blank)//10+2) :
        if blank[(i-1)*10:i*10] :
            print("".join(blank[(i-1)*10:i*10]))


