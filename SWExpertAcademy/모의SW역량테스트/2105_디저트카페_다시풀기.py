"""
디저트 카페
"""
def isNotWall(x,y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

dx = [-1,1,1,-1]
dy = [1,1,-1,-1]

def eatDessert(x,y, a,b, d1,d2,d3,d4) :
    if d1 < a :
        # 벽이 아니고 이전에 먹은 디저트가 아니라면, 고!
        if isNotWall(x+dx[0],y+dy[0]) and dessert[board[x+dx[0]][y+dy[0]]] == False :
            dessert[board[x + dx[0]][y + dy[0]]] = True
            eatDessert(x+dx[0],y+dy[0], a, b, d1+1, d2, d3, d4)
    elif d2 < b :
        if isNotWall(x+dx[1],y+dy[1]) and dessert[board[x+dx[1]][y+dy[1]]] == False :
            dessert[board[x + dx[1]][y + dy[1]]] = True
            eatDessert(x+dx[1],y+dy[1], a, b, d1, d2+1, d3, d4)
    elif d3 < a :
        if isNotWall(x+dx[2],y+dy[2]) and dessert[board[x+dx[2]][y+dy[2]]] == False :
            dessert[board[x + dx[2]][y + dy[2]]] = True
            eatDessert(x+dx[2],y+dy[2], a, b, d1, d2, d3+1, d4)
    elif d4 < b :
        if isNotWall(x+dx[3],y+dy[3]) and dessert[board[x+dx[3]][y+dy[3]]] == False :
            dessert[board[x + dx[3]][y + dy[3]]] = True
            eatDessert(x+dx[3],y+dy[3], a, b, d1, d2, d3, d4+1)
    elif d4 == b :
        global maxDessert
        maxDessert = max(maxDessert, (a+b)*2)

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxDessert = 0
    # 두 변의 합은 N-1을 넘어선 안되며, 한 변의 최대 길이는 N-2이다.
    # 시작점 x는 1~N-2, y는 0~ N-3이다
    for x in range(1, N-1) :
        for y in range(N-2) :
            # x, y를 시작점으로 가능한 모든 경로를 계산한다.
            for i in range(1,N-1) :
                for j in range(1,N-i) :
                    dessert = [False]*101
                    eatDessert(x, y, i, j, 0, 0, 0, 0)

    if maxDessert == 0 :
        maxDessert = -1
    print('#{} {}'.format(test_case, maxDessert))

"""
1
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
"""