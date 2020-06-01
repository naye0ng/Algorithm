"""
사다리조작
https://www.acmicpc.net/problem/15684
"""
# 왼, 아, 오
dy = [-1,0,1]

# 사다리 결과 확인
def check_result() :
    for start in range(N) :
        x, y = 0, start
        while x < H :
            y += dy[board[x][y]]
            x += 1
        if y != start :
            return False

    return True

# 다리 생성
def make_bridge(i, cnt) :
    global min_bridge
    if cnt < min_bridge :
        if check_result() :
            min_bridge = cnt
        else :
            for j in range(i, len(bridge)) :
                # j번째 bridge에 다리 놓기
                if board[bridge[j][0]][bridge[j][1]] == 1 and board[bridge[j][0]][bridge[j][1]+1] == 1 :
                    board[bridge[j][0]][bridge[j][1]], board[bridge[j][0]][bridge[j][1]+1] = 2, 0
                    make_bridge(j+1, cnt+1)
                    board[bridge[j][0]][bridge[j][1]], board[bridge[j][0]][bridge[j][1]+1] = 1, 1

N, M, H = map(int, input().split())
board = [[1]*N for _ in range(H)]
for _ in range(M) :
    a, b = map(int, input().split())
    board[a-1][b-1], board[a-1][b] = 2, 0

# 생성가능한 다리 위치
bridge = []
for a in range(H) :
    for b in range(N-1) :
        if board[a][b] == 1 and board[a][b+1] == 1 :
            bridge.append([a,b])

min_bridge = 4
make_bridge(0, 0)
if min_bridge == 4 :
    min_bridge = -1
print(min_bridge)
