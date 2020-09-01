"""
청소년 상어
https://www.acmicpc.net/problem/19236
"""
import copy 

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def is_not_wall(x, y) :
    if x < 0 or x >= 4 : return False
    if y < 0 or y >= 4 : return False
    return True

def move_fish(board, fishes, eaten, shark, fish_sum) :
    for i in range(1, 17) :
        if eaten[i] : continue
        x, y, d = fishes[i]
        if board[x][y] == -1 : print(i, eaten, fishes[i])

        if is_not_wall(x+dx[d], y+dy[d]) and board[x+dx[d]][y+dy[d]] >= 0 :
            fishes[i][0], fishes[i][1] = x+dx[d], y+dy[d]
            swap_fish = board[x+dx[d]][y+dy[d]]
            if swap_fish :
                fishes[swap_fish][0], fishes[swap_fish][1] = x, y
            board[x][y], board[x+dx[d]][y+dy[d]] = board[x+dx[d]][y+dy[d]], board[x][y]
            
        else :
            for j in range(8) :
                if is_not_wall(x+dx[(d+j)%8], y+dy[(d+j)%8]) and board[x+dx[(d+j)%8]][y+dy[(d+j)%8]] >= 0 :
                    fishes[i] = [x+dx[(d+j)%8], y+dy[(d+j)%8], (d+j)%8]
                    swap_fish = board[x+dx[(d+j)%8]][y+dy[(d+j)%8]]
                    if swap_fish :
                        fishes[swap_fish][0], fishes[swap_fish][1] = x, y
                    board[x][y], board[x+dx[(d+j)%8]][y+dy[(d+j)%8]] = board[x+dx[(d+j)%8]][y+dy[(d+j)%8]], board[x][y]
                    break
    eat_fish(board, fishes, eaten, shark, fish_sum)

def eat_fish(board, fishes, eaten, shark, fish_sum) :
    x, y, d = shark
    for i in range(1, 4) :
        if is_not_wall(x+dx[d]*i, y+dy[d]*i) and board[x+dx[d]*i][y+dy[d]*i] > 0 :
            fish = board[x+dx[d]*i][y+dy[d]*i]
            eaten[fish] = True
            board[x][y], board[x+dx[d]*i][y+dy[d]*i] = 0, -1
            move_fish(copy.deepcopy(board), copy.deepcopy(fishes), eaten, [x+dx[d]*i, y+dy[d]*i, fishes[fish][2]], fish_sum+fish)
            board[x][y], board[x+dx[d]*i][y+dy[d]*i] = -1, fish
            eaten[fish] = False

    global sum_of_fish
    sum_of_fish =max(sum_of_fish, fish_sum)

board = [[0]*4 for _ in range(4)]
fishes = [0]*17

arr = [list(map(int, input().split())) for _ in range(4)]
for x in range(4) :
    for y in range(4): 
        board[x][y] = arr[x][y*2]
        fishes[arr[x][y*2]] = [x, y, arr[x][y*2+1]-1]

sum_of_fish = 0
eaten = [False]*17

fish = board[0][0]
shark = fishes[fish]
eaten[fish] = True
board[0][0] = -1

move_fish(board, fishes, eaten, shark, fish)
print(sum_of_fish)

