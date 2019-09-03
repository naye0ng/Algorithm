"""
5658 - 보물상자 비밀번호
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE
"""
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    alpha = input()
    n16 = set()
    
    # N//4번 회전
    for _ in range(N//4) :
        n16.add(alpha[:N//4]) 
        n16.add(alpha[N//4:N//4*2])
        n16.add(alpha[N//4*2:N//4*3])
        n16.add(alpha[N//4*3:N])
        alpha = alpha[-1]+alpha[:-1]
    print('#{} {}'.format(test_case, int(sorted(list(n16), reverse=True)[K-1], 16) ))


# python 진수 변환 : https://doriri.tistory.com/30