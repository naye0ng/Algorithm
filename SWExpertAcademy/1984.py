"""
1984. 중간 평균값 구하기
"""
T = int(input())
for test_case in range(1,T+1):
    an = list(map(int, input().split()))

    sumAn = 0
    max_i , min_i = 0, 0

    for i in range(len(an)) :
        if an[i] > an[max_i] :
            max_i = i
        if an[i] < an[min_i] :
            min_i = i

    for i in range(0,len(an)) :
        if i == max_i or i == min_i :
            continue
        sumAn += an[i]

    print(f'#{test_case} {round(sumAn/(len(an)-2))}')