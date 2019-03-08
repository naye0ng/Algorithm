"""
4615.재미있는 오셀로 게임
"""
import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
def isNotWall(x,y) :
    global N
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True

def putStone(Stone) :
    global black, white
    x, y, color = Stone[1]-1, Stone[0]-1, Stone[2]
    board[x][y] = color
    if color == 1 :
        black +=1
    else :
        white +=1

    # 가로, 세로, 대각선 체크
    for i in range(8) :
        x2 = x+dx[i]
        y2 = y+dy[i]

      
        # check의 경우 앞 쪽에 자신과 같은 색의 돌이 있는지 체크
        num, check = 0, 0
        while isNotWall(x2, y2) :
            if board[x2][y2] == 3-color :
                num += 1
                x2 += dx[i]
                y2 += dy[i]
            else :
                # 0과 자기자신의 경우
                if board[x2][y2] == color :
                    check = 1
                break
        # 변경할 값이 있다면
        if num and check :
            for k in range(1,num+1) :
                board[x+dx[i]*k][y+dy[i]*k] = color
            if color == 1 :
                black +=num
                white -= num
            else :
                black -=num
                white += num

T = int(input())
for test_case in range(1,1+T) :
    N , M = map(int, input().split())

    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] =1

    black, white = 2, 2
    for _ in range(M) :
        putStone(list(map(int, input().split())))

    print('#{} {} {}'.format(test_case,black,white))