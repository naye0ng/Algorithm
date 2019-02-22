"""
5431.민석이의 과제 체크하기
"""
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    kn = list(map(int,input().split()))

    print(f'#{test_case}', end=' ')
    for i in range(1,n+1) :
        if i not in kn :
            print(i,end=' ')

    print()

