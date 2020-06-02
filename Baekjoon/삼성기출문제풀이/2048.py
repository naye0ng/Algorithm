"""
2048
https://www.hun-s.com/product/detail.html?product_no=13438&cate_no=42&display_group=1
"""
import copy

def up(board, move) :
    if move == 5 :
        global max_value
        max_value = max(max_value, max( max(board[x]) for x in range(N)))
    else :
        visited = [[0]*N for _ in range(N)]
        for y in range(N) :
            for x in range(1, N) :
                if board[x][y] == 0 :
                    continue
                while x > 0 :
                    if board[x-1][y] == 0 :
                        board[x-1][y], board[x][y] = board[x][y], board[x-1][y]
                    elif not visited[x-1][y] and board[x-1][y] == board[x][y] :
                        visited[x-1][y] = 1
                        board[x-1][y], board[x][y] = board[x][y]*2, 0
                        break
                    else :
                        break
                    x -= 1
        up(copy.deepcopy(board), move+1)
        down(copy.deepcopy(board), move+1)
        left(copy.deepcopy(board), move+1)
        right(copy.deepcopy(board), move+1)

        
def down(board, move) :
    if move == 5 :
        global max_value
        max_value = max(max_value, max( max(board[x]) for x in range(N)))
    else :
        visited = [[0]*N for _ in range(N)]
        for y in range(N) :
            for x in range(N-2, -1, -1) :
                if board[x][y] == 0 :
                    continue
                while x < N-1 :
                    if board[x+1][y] == 0 :
                        board[x+1][y], board[x][y] = board[x][y], board[x+1][y]
                    elif not visited[x+1][y] and board[x+1][y] == board[x][y] :
                        visited[x+1][y] = 1
                        board[x+1][y], board[x][y] = board[x][y]*2, 0
                        break
                    else :
                        break
                    x += 1
        up(copy.deepcopy(board), move+1)
        down(copy.deepcopy(board), move+1)
        left(copy.deepcopy(board), move+1)
        right(copy.deepcopy(board), move+1)

def left(board, move) :
    if move == 5 :
        global max_value
        max_value = max(max_value, max( max(board[x]) for x in range(N)))
    else :
        visited = [[0]*N for _ in range(N)]
        for x in range(N) :
            for y in range(1, N) :
                if board[x][y] == 0 :
                    continue
                while y > 0 :
                    if board[x][y-1] == 0 :
                        board[x][y-1], board[x][y] = board[x][y], board[x][y-1]
                    elif not visited[x][y-1] and board[x][y-1] == board[x][y] :
                        visited[x][y-1] = 1
                        board[x][y-1], board[x][y] = board[x][y]*2, 0
                        break
                    else :
                        break
                    y -= 1
        up(copy.deepcopy(board), move+1)
        down(copy.deepcopy(board), move+1)
        left(copy.deepcopy(board), move+1)
        right(copy.deepcopy(board), move+1)

def right(board, move) :
    if move == 5 :
        global max_value
        max_value = max(max_value, max( max(board[x]) for x in range(N)))
    else :
        visited = [[0]*N for _ in range(N)]
        for x in range(N) :
            for y in range(N-2, -1, -1) :
                if board[x][y] == 0 :
                    continue
                while y < N-1 :
                    if board[x][y+1] == 0 :
                        board[x][y+1], board[x][y] = board[x][y], board[x][y+1]
                    elif not visited[x][y+1] and board[x][y+1] == board[x][y] :
                        visited[x][y+1] = 1
                        board[x][y+1], board[x][y] = board[x][y]*2, 0
                        break
                    else :
                        break
                    y += 1
        up(copy.deepcopy(board), move+1)
        down(copy.deepcopy(board), move+1)
        left(copy.deepcopy(board), move+1)
        right(copy.deepcopy(board), move+1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

up(copy.deepcopy(board), 0)
down(copy.deepcopy(board), 0)
left(copy.deepcopy(board), 0)
right(copy.deepcopy(board), 0)
print(max_value)

"""
8
2 2 2 2 2 2 0 0
2 2 4 2 2 2 0 0
0 0 0 2 2 2 0 0
0 0 0 2 2 2 0 0
4 4 4 2 2 2 0 0
0 0 0 2 2 2 0 0
2 4 4 2 2 2 0 0
2 2 2 2 2 2 0 0
"""