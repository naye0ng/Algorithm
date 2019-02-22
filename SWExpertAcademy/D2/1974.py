"""
1974.스토쿠 검증
"""
T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    breaker = False
    for i in range(9):
        if breaker:
            break

        rownum = {k: 0 for k in range(1, 10)}
        colnum = {k: 0 for k in range(1, 10)}
        crossnum = {k: 0 for k in range(1, 10)}
        for j in range(9):
            if rownum[sudoku[i][j]] == 1 or colnum[sudoku[j][i]] == 1 or crossnum[
                sudoku[(j // 3) + (i // 3) * 3][(j % 3) + (i % 3) * 3]] == 1:
                result = 0
                breaker = True
                break
            # 나온 값 체크
            rownum[sudoku[i][j]] = 1
            colnum[sudoku[j][i]] = 1
            crossnum[sudoku[(j // 3) + (i // 3) * 3][(j % 3) + (i % 3) * 3]] = 1

    print(f'#{test_case} {result}')