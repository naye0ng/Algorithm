'''
Gaaaaaaaaaarden
https://www.acmicpc.net/problem/18809
'''
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def is_not_wall(x, y) :
    global N, M
    if x < 0 or x >= N : return False
    if y < 0 or y >= M : return False
    return True

def spread_cell(garden, GR) :
    global N, M
    visited = [[0 if garden[x][y] != 1 else N*M for y in range(M)] for x in range(N)]

    flower, t = 0, 0
    while GR :
        t += 1
        for _ in range(len(GR)) :
            x, y, color = GR.pop(0)
            if garden[x][y] == color :
                for i in range(4) :
                    if is_not_wall(x+dx[i], y+dy[i]) and visited[x+dx[i]][y+dy[i]] >= t and garden[x+dx[i]][y+dy[i]]:
                        color2 = garden[x+dx[i]][y+dy[i]]
                        if color2 == color or color2 == 'F': continue
                        if color2 == 1 :
                            garden[x+dx[i]][y+dy[i]] = color
                            visited[x+dx[i]][y+dy[i]] = t
                            GR.append([x+dx[i], y+dy[i], color])
                        elif color2 != color :
                            flower += 1
                            garden[x+dx[i]][y+dy[i]] = 'F'

    global answer
    answer = max(answer, flower)

def drop_cell(G, R, green, red, i = 0) :
    if G == 0 and R == 0 :
        spread_cell(copy.deepcopy(garden), green+red)
    else :
        for k in range(i, len(cell)) :
            x, y = cell[k]
            if G :
                garden[x][y] = 'G'
                drop_cell(G-1, R, green+[[x, y, 'G']], red, k+1)
            if R :
                garden[x][y] = 'R'
                drop_cell(G, R-1, green, red+[[x, y, 'R']], k+1)
            garden[x][y] = 1


N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

cell = []
for x in range(N) :
    for y in range(M) :
        if garden[x][y] == 2 :
            cell.append([x, y])
            garden[x][y] = 1

answer = 0
drop_cell(G, R, [], [])
print(answer)