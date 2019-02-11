"""
1210.사다리(Ladder1)
"""
for t in range(10):
    test_case = int(input())

    # 가벽 세우기, 100x102행렬이 생성됨
    path = [list(map(int, ("0 " + input() + " 0").split())) for i in range(100)]

    # 시작점의 y좌표 찾기
    for i in range(1, 101):
        if path[99][i] == 2:
            y = i
            break

    # 올라가기
    x = 99

    while x > 0:
        # 양옆 체크, 지나간 곳 체크
        if path[x][y - 1] == 1:
            path[x][y] = 0
            y -= 1
        elif path[x][y + 1] == 1:
            path[x][y] = 0
            y += 1
        else:
            # 양옆이 없음 올라감
            x -= 1

    print(f'#{test_case} {y - 1}')