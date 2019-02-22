"""
1220.Magnetic

"""
for test_case in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    total = 0
    for y in range(n):
        color = 0
        colsum = 0
        for x in range(n):
            if table[x][y] == 0:
                continue

            # 첫번째 값이 red이면(첫번째에 블루가 나옴 버림)
            if color == 0 and table[x][y] == 1:
                color = 1
                colsum += 1
            # 이전 컬러가 blue인데 지금이 red라면, +1
            elif color == 2 and table[x][y] == 1:
                color = table[x][y]
                colsum += 1

            else:
                color = table[x][y]

        # 마지막 색상이 red이면 -1
        if color == 1:
            colsum -= 1
        total += colsum

    print(f'#{test_case} {total}')



