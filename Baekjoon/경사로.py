"""
경사로 - 시뮬레이션(경우의 수를 다 생각해봐야함 >> 실수하기 쉬움)
https://www.acmicpc.net/problem/14890
""" 
# 수평 검사, x 고정
def horizental(x, N, L) :
    h = board[x][0]
    same_h = 1
    slope_w = 0
    is_posible = True
  
    for y in range(1,N) :
        if slope_w :
            # 경사로 설치중
            if board[x][y] == h :
                slope_w -= 1
                # 경사로 설치 끝
                if slope_w == 0 :
                    is_posible = True
            else :
                is_posible = False
                break
        else :

            if board[x][y] == h :
                same_h += 1
            elif (board[x][y] - h) == 1 :
                if same_h >= L :
                    # 이전 경로상에 설치 가능
                    h = board[x][y]
                    same_h = 1
                else :
                    is_posible = False
                    break
            elif (board[x][y] - h)  == -1 :
                slope_w = L-1
                h = board[x][y]
                same_h = 0
                if slope_w :
                    is_posible = False
            else :
                is_posible = False
                break
    return is_posible
    
def vertical(y, N, L) :
    h = board[0][y]
    same_h = 1
    slope_w = 0
    is_posible = True
  
    for x in range(1, N) :
        if slope_w :
            # 경사로 설치중
            if board[x][y] == h :
                slope_w -= 1
                # 경사로 설치 끝
                if slope_w == 0 :
                    is_posible = True
            else :
                is_posible = False
                break
        else :
            if board[x][y] == h :
                same_h += 1
            elif (board[x][y] - h) == 1 :
                if same_h >= L :
                    # 이전 경로상에 설치 가능
                    h = board[x][y]
                    same_h = 1
                else :
                    is_posible = False
                    break
            elif (board[x][y] - h)  == -1 :
                slope_w = L-1
                h = board[x][y]
                same_h = 0
                if slope_w :
                    is_posible = False
            else :
                is_posible = False
                break
    return is_posible


N, L = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]

result = 0
for x in range(N) :
    for y in range(N) :
        if y == 0 : 
            result += horizental(x, N, L)
        if x == 0 : 
            result += vertical(y, N, L)

print(result)

