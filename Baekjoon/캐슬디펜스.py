"""
캐슬디펜스
https://www.acmicpc.net/problem/17135
"""
max_enemy = 0
def castle_defence(P) :
    enemy = []
    for x in range(N) :
        for y in range(M) :
            if board[x][y] == 1 :
                enemy.append([x,y])

    die_enemy = 0
    while enemy :
        # [1] 거리가 D 이내에 있는 적 찾아서 공격
        dist = [D+1]*3
        die_idx = [-1]*3
        for i in range(len(enemy)) :
            for j in range(3) :
                d = (N - enemy[i][0]) + abs(P[j]- enemy[i][1])
                if d <= D :
                    if d < dist[j]:
                        dist[j], die_idx[j] = d, i
                    # 왼쪽에 더 가까운 값
                    elif d == dist[j] and enemy[i][1] < enemy[die_idx[j]][1] :
                        dist[j], die_idx[j] = d, i
                        
        for idx in sorted(list(set(die_idx)),reverse=True) :
            if idx >= 0 :
                enemy.pop(idx)
                die_enemy += 1

        # 이동
        for _ in range(len(enemy)) :
            x,y = enemy.pop(0)
            if x+1 < N :
                enemy.append([x+1, y])
    global max_enemy
    max_enemy = max(max_enemy, die_enemy)

# 궁수 배치
def archer(n, k, position) :
    if n == 3 :
        castle_defence(position)
    else :
        for i in range(k+1, M) :
            archer(n+1, i, position+[i])

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

archer(0,-1,[])
print(max_enemy)