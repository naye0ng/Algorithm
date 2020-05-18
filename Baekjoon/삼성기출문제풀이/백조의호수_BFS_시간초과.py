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

def have_they_met(sx, sy) :
    visited = [[False]*C for _ in range(R)]
    visited[sx][sy] = True
    queue = [[sx, sy]]
    while queue :
        x, y = queue.pop(0)
        for i in range(4) :
            if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                visited[x+dx[i]][y+dy[i]] = True
                if lake[x+dx[i]][y+dy[i]] == "." :
                    queue.append([x+dx[i],y+dy[i]])
                elif lake[x+dx[i]][y+dy[i]] == "L" : 
                    return True
    return False
    
def melt() :
    visited = [[False]*C for _ in range(R)]
    for x in range(R) :
        for y in range(C) :
            if not visited[x][y] and lake[x][y] =='.' :
                visited[x][y] = True
                queue = [[x,y]]
                while queue :
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if is_not_wall(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
                            visited[x+dx[i]][y+dy[i]] = True
                            if lake[x+dx[i]][y+dy[i]] == "." :
                                queue.append([x+dx[i],y+dy[i]])
                            elif lake[x+dx[i]][y+dy[i]] == "X" : 
                                lake[x+dx[i]][y+dy[i]] = "."

R, C = map(int, input().split())
lake = [" ".join(input()).split(" ") for _ in range(R)]

sx, sy = 0, 0
for x in range(R) :
    for y in range(C) :
        if lake[x][y] == 'L' :
            sx, sy = x, y
            break

day = 0
while not have_they_met(sx, sy) :
    melt()
    day += 1
    
print(day)