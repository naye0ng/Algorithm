"""
디저트카페
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
"""
"""
[오늘의 교훈]
어차피 SWEA 서버는 체크 함수 만든다고 터지지 않는다.
그냥 오래걸리더라도 분리하자!
"""
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

dx = [-1,1,1,-1]
dy = [1,1,-1,-1]
def eat_dessert(x, y, d, d1, d2, d3, d4) :
    if d == 0 :
        if is_not_wall(x+dx[d],y+dy[d]) and not dessert[road[x+dx[d]][y+dy[d]]] : 
            dessert[road[x+dx[d]][y+dy[d]]] = True
            eat_dessert(x+dx[d], y+dy[d], d, d1+1, d2, d3, d4)
            dessert[road[x+dx[d]][y+dy[d]]] = False
        if d1 >= 1 and is_not_wall(x+dx[d+1],y+dy[d+1]) and not dessert[road[x+dx[d+1]][y+dy[d+1]]] :
            dessert[road[x+dx[d+1]][y+dy[d+1]]] = True
            eat_dessert(x+dx[d+1], y+dy[d+1], d+1, d1, d2+1, d3, d4)
            dessert[road[x+dx[d+1]][y+dy[d+1]]] = False
    elif d == 1 :
        if is_not_wall(x+dx[d],y+dy[d]) and not dessert[road[x+dx[d]][y+dy[d]]] : 
            dessert[road[x+dx[d]][y+dy[d]]] = True
            eat_dessert(x+dx[d], y+dy[d], d, d1, d2+1, d3, d4)
            dessert[road[x+dx[d]][y+dy[d]]] = False
        if d2 >= 1 and is_not_wall(x+dx[d+1],y+dy[d+1]) and not dessert[road[x+dx[d+1]][y+dy[d+1]]] :
            dessert[road[x+dx[d+1]][y+dy[d+1]]] = True
            eat_dessert(x+dx[d+1], y+dy[d+1], d+1, d1, d2, d3+1, d4)
            dessert[road[x+dx[d+1]][y+dy[d+1]]] = False
    elif d == 2 :
        if d3 == d1 :
            if is_not_wall(x+dx[d+1],y+dy[d+1]) and not dessert[road[x+dx[d+1]][y+dy[d+1]]] :
                dessert[road[x+dx[d+1]][y+dy[d+1]]] = True
                eat_dessert(x+dx[d+1], y+dy[d+1], d+1, d1, d2, d3, d4+1)
                dessert[road[x+dx[d+1]][y+dy[d+1]]] = False
        elif is_not_wall(x+dx[d],y+dy[d]) and not dessert[road[x+dx[d]][y+dy[d]]] :
            dessert[road[x+dx[d]][y+dy[d]]] = True
            eat_dessert(x+dx[d], y+dy[d], d, d1, d2, d3+1, d4)
            dessert[road[x+dx[d]][y+dy[d]]] = False
    elif d == 3 :
        if d4 == d2 :
            global result
            result = max(result, (d1+d2)*2)
        elif is_not_wall(x+dx[d],y+dy[d]) and not dessert[road[x+dx[d]][y+dy[d]]] :
            dessert[road[x+dx[d]][y+dy[d]]] = True
            eat_dessert(x+dx[d], y+dy[d], d, d1, d2, d3, d4+1)
            dessert[road[x+dx[d]][y+dy[d]]] = False

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    dessert = [False]*101

    result = -1
    for x in range(1,N-1) :
        for y in range(N-2) :
            eat_dessert(x, y, 0, 0, 0, 0, 0) 

    print('#{} {}'.format(test_case, result))