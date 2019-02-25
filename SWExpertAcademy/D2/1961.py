"""
1961.숫자 배열의 회전
"""
def change90(target) :
    global n
    temps = [[0]*n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            temps[i][j] = target[n-1-j][i]

    return temps

T = int(input())
for test_case in range(1,T+1) :
    n = int(input())
    an = [input().split() for _ in range(n)]


    an90 = change90(an)
    an180 = change90(an90)
    an270 = change90(an180)

    print(f'#{test_case}')
    for k in range(n) :
        print(f'{"".join(an90[k])} {"".join(an180[k])} {"".join(an270[k])}')
