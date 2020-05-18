""" 
백조의호수
https://www.acmicpc.net/problem/3197
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= R :
        return False
    if y < 0 or y >= C :
        return False
    return True
    
# DFS : 백조가 서로 만날 수 있는 최단 기간
def get_shortest_day(x, y, day) :
    global shortest_day
    if x == swans[1][0] and y == swans[1][1] :
        shortest_day = min(shortest_day, day)
    else :
        for i in range(4) :
            if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                new_day = max(day, malt_time[x+dx[i]][y+dy[i]])
                if new_day < shortest_day :
                    visited[x+dx[i]][y+dy[i]] =  True
                    get_shortest_day(x+dx[i], y+dy[i], new_day) 
                    visited[x+dx[i]][y+dy[i]] =  False

R, C = map(int, input().split())
lake = [" ".join(input()).split(" ") for _ in range(R)]
malt_time = [[R*C]*C for _ in range(R)]

swans, queue = [], []
for x in range(R) :
    for y in range(C) :
        if lake[x][y] == 'L' :
            swans.append([x,y])
            lake[x][y] = '.'

        if lake[x][y] == '.' :
            queue.append([x,y])
            malt_time[x][y] = 0

# DP : 얼음이 녹는 시간
while queue :
    x, y = queue.pop(0)
    for i in range(4) :
        if is_not_wall(x+dx[i], y+dy[i]) and malt_time[x+dx[i]][y+dy[i]] > malt_time[x][y]+1 :
            malt_time[x+dx[i]][y+dy[i]] = malt_time[x][y]+1
            queue.append([x+dx[i], y+dy[i]])

shortest_day = R*C
x, y = swans[0]
visited = [[False]*C for _ in range(R)]
visited[x][y] = True
get_shortest_day(x, y, 0) 

print(shortest_day)


"""
매번 얼음을 녹이고 다시 BFS를 하지 않고, 과정을 진행하면서 얼음을 녹이는 방법을 생각해 보세요.
즉, 전체에서 BFS가 딱 한 번만 돌아야 합니다. 또는 union find 등을 사용할 수도 있습니다.
"""

"""
8 17
...XXXXXX..XX.XXX
....XXXX.XXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
"""
