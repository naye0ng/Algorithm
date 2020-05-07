"""
보물상자비밀번호
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
"""

T = int(input())
for test_case in range(1, 1+T) :
    N, K = map(int, input().split())
    S = " ".join(input()).split()

    numbers = set()
    for i in range(N) :
        num = ''
        for j in range(N//4) :
            num += S[(i+j)%N]
        numbers.add(int(num, 16))

    print('#{} {}'.format(test_case, sorted(numbers, reverse=True)[K-1]))

"""
1
16 2
F53586D76286B2D8
"""