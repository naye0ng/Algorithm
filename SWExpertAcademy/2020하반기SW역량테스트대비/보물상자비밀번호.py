'''
보물상자비밀번호
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE
'''
T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    S = ' '.join(input()).split(' ')

    numbers = set()
    l = N//4
    for _ in range(l) :
        numbers.add(int(''.join(S[:l]), 16))
        numbers.add(int(''.join(S[l:l*2]), 16))
        numbers.add(int(''.join(S[l*2:l*3]), 16))
        numbers.add(int(''.join(S[l*3:]), 16))

        S.append(S.pop(0))

    print('#{} {}'.format(test_case, sorted(list(numbers), reverse = True)[K-1]))