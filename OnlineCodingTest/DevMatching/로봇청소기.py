dx = [-1,0,1,0]
dy = [0,1,0,-1]
N = 0
def is_not_wall(x, y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def solution(office, x, y, move):
    global N
    N = len(office)

    # 처음에 로봇은 북쪽을 바라보고 있으며, 현재 칸을 청소합니다.
    answer = office[x][y]
    office[x][y] = 0
    d = 0
    for m in move :
        if m == "go" :
            if is_not_wall(x+dx[d], y+dy[d]) and office[x+dx[d]][y+dy[d]] >= 0 :
                x += dx[d]
                y += dy[d]
                answer += office[x][y]
                office[x][y] = 0
        elif m == "right" :
            d = (d+1)%4
        elif m == "left" :
            d = (d-1)%4

    return answer




print(solution(	[[5, -1, 4], [6, 3, -1], [2, -1, 1]], 1, 0, ["go", "go", "right", "go", "right", "go", "left", "go"]))