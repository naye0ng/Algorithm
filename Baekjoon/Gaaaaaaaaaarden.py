"""
Gaaaaaaaaaarden
https://www.acmicpc.net/problem/18809
"""
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

def spread_cell(garden) :
    time = [[250]*M for _ in range(N)]
    queue = []
    for x in range(N) :
        for y in range(M) :
            if garden[x][y] >= 3 :
                time[x][y] = 0
                queue.append([x, y, 0])
    flower = 0
    while queue :
        x, y, t = queue.pop(0)
        """
        [주의] 퍼진 뒤에 꽃이 된 경우를 체크!
        """
        if garden[x][y] != 0 :
            for i in range(4) :
                # 벽, 물이 아니고 이전에 퍼진적이 없을 때
                if is_not_wall(x+dx[i], y+dy[i]) and garden[x+dx[i]][y+dy[i]] != 0 and time[x+dx[i]][y+dy[i]] >= t+1:
                    # 빈칸이면 퍼짐
                    if garden[x+dx[i]][y+dy[i]] <= 2 :
                        garden[x+dx[i]][y+dy[i]] = garden[x][y]
                        time[x+dx[i]][y+dy[i]] = t+1
                        queue.append([x+dx[i], y+dy[i], t+1])
                    # 꽃이 핀적 없고 다른 색상이면 꽃핌 + 안퍼짐
                    elif garden[x+dx[i]][y+dy[i]] != garden[x][y] :
                        garden[x+dx[i]][y+dy[i]] = 0
                        time[x+dx[i]][y+dy[i]] = t+1
                        flower += 1
    global total_flower
    total_flower = max(total_flower, flower)


def drop_cell(n, k, green, red) :
    if n == G+R :
        # 퍼트리기
        spread_cell(copy.deepcopy(garden))
    else :
        for j in range(k,len(cell)-(green+red)+1) :
            x, y =  cell[j]
            if green :
                garden[x][y] = 3
                drop_cell(n+1, j+1, green-1, red)
                garden[x][y] = 2
            if red :
                garden[x][y] = 4
                drop_cell(n+1, j+1, green, red-1)
                garden[x][y] = 2

N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

cell = []
for x in range(N) :
    for y in range(M) :
        if garden[x][y] == 2 :
            cell.append([x,y])

total_flower = 0
drop_cell(0, 0, G, R)
print(total_flower)