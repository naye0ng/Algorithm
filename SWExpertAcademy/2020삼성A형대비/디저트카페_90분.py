"""
디저트카페
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE
"""
dx = [-1,1,1,-1]
dy = [1,1,-1,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def eat_dessert(x, y, d, cnt, eaten) :
    # 원점으로 돌아오면 끝
    if d == 3 and direction[0] == direction[2] and direction[1] == direction[3] :
        global dessert
        dessert = max(dessert, cnt)
    else :
        while True :
            # 현재 방향으로 한번 더 이동
            if is_not_wall(x+dx[d], y+dy[d]) and board[x+dx[d]][y+dy[d]] not in eaten :
                direction[d] += 1
                eat_dessert(x+dx[d], y+dy[d], d, cnt+1, eaten+[board[x+dx[d]][y+dy[d]]])
                direction[d] -= 1

            # 현재 위치에 왔던 적이 1번 이상이고, d < 3이면 방향을 바꿀수도 있다.
            if d < 3 and direction[d] >= 1 :
                d += 1
            else :
                break


T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dessert = -1
    direction = [0]*4
    for x in range(1, N-1) :
        for y in range(N-2) :
            eat_dessert(x, y, 0, 0, [])

    print('#{} {}'.format(test_case, dessert))