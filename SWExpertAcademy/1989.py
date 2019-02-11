"""
1989.초심자의 회문 검사
"""
T = int(input())
for test_case in range(1,T+1):
    an = input().replace(""," ").split()

    result = 1
    for i in range(len(an)//2):
        if an[i] != an[len(an)-1-i] :
            result = 0
            break

    print(f'#{test_case} {result}')
