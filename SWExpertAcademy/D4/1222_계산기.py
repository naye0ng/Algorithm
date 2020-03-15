"""
계산기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD&categoryId=AV14mbSaAEwCFAYD&categoryType=CODE
"""

for test_case in range(1, 11):
    L = input()
    S = list(map(int,input().split('+')))

    # 후위 표기법으로 바꿔서 계산하기
    result = S[0]
    for i in range(1,len(S)) :
        result += S[i]

    print(f'#{test_case} {result}')