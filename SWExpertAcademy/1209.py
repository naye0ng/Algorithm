"""
1209.sum

(라이브러리 사용 금지)
100X100의 2차원 배열이 주어질 때, 
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구해라
"""

for i in range(10) :
    test_case = int(input())

    an = [list(map(int, input().split())) for i in range(100)]

    max_row = max_col = max_cross = sum_cross = sum_cross2 = 0
    k = len(an)-1
    for i in range(len(an)) :
        sum_row = sum_col = 0
        for j in range(len(an[i])) :
            sum_row += an[i][j]
            sum_col += an[j][i]
            if i == j :
                sum_cross +=an[i][j]
            if j-i == k :
                sum_cross2 += an[i][j]
                k-=2
        if max_row < sum_row :
            max_row = sum_row
        
        if max_col < sum_col :
            max_col = sum_col
    
        if sum_cross < sum_cross2 :
            max_cross = sum_cross2
        else :
            max_cross = sum_cross

    if max_col > max_row :
        if max_col > max_cross :
            print(f'#{test_case} {max_col}')
        else :
            print(f'#{test_case} {max_cross}')
    else :
        if max_row > max_cross :
            print(f'#{test_case} {max_row}')
        else :
            print(f'#{test_case} {max_cross}')
    
