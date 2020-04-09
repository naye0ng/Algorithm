"""
등산로 조성
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True
        
def make_long_road(x, y, D, can_cut) :
    global max_dist
    max_dist = max(max_dist, D)

    for i in range(4) :
        if is_not_wall(x+dx[i],y+dy[i]) and not visited[x+dx[i]][y+dy[i]] :
            if board[x+dx[i]][y+dy[i]] < board[x][y] :
                visited[x+dx[i]][y+dy[i]] = True
                make_long_road(x+dx[i], y+dy[i], D+1, can_cut)
                visited[x+dx[i]][y+dy[i]] = False
            elif can_cut and board[x+dx[i]][y+dy[i]]-K < board[x][y] :
                visited[x+dx[i]][y+dy[i]] = True
                """
                k == 3, 현재위치 5, 이동할 곳에 6이 있는 상황
                2뺴줘야 하는데 2는 6-(6-5+1) = 4 => 5-1(항상 1 장은 상황이 제일 적당함)
                """
                original_value, board[x+dx[i]][y+dy[i]] = board[x+dx[i]][y+dy[i]], board[x][y] - 1
                make_long_road(x+dx[i], y+dy[i], D+1, False)
                board[x+dx[i]][y+dy[i]] = original_value
                visited[x+dx[i]][y+dy[i]] = False


T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    max_dist = 0

    start_point, value = [],  0
    for x in range(N) :
        for y in range(N) :
            if board[x][y] == value :
                start_point.append([x,y])
            elif board[x][y] > value :
                value = board[x][y]
                start_point = [[x,y]]
    for x, y in start_point :
        visited[x][y] = True
        make_long_road(x, y, 1, True)
        visited[x][y] = False

    print('#{} {}'.format(test_case, max_dist))