"""
2048
https://www.acmicpc.net/problem/12100
"""
import copy

def moveLeft(N, board, depth) :
    if depth == 5 :
        return getMax(N, copy.deepcopy(board))
    else :
        visited = [[False]*N for _ in range(N)]
        for x in range(N) :
            y = 1
            while y < N :
                if board[x][y] != 0 :
                    y2 = y
                    for k in range(y2-1,-1,-1) :
                        if board[x][k] == 0 :
                            board[x][k], board[x][y2] = board[x][y2], board[x][k]
                            visited[x][k], visited[x][y2] = visited[x][y2], visited[x][k]
                        elif  board[x][k] == board[x][y2] and visited[x][k] == False and visited[x][y2] == False:
                            board[x][k] = board[x][k]*2
                            board[x][y2] = 0
                            visited[x][k] = True
                        else :
                            break
                        y2 = k
                y += 1
        return max(
                moveBottom(N, copy.deepcopy(board), depth+1),
                moveTop(N, copy.deepcopy(board), depth+1),
                moveRight(N, copy.deepcopy(board),depth+1),
                moveLeft(N, copy.deepcopy(board), depth+1)
                )
                
def moveRight(N, board, depth) :
    if depth == 5 :
        return getMax(N, copy.deepcopy(board))
    else :
        visited = [[False]*N for _ in range(N)]
        for x in range(N) :
            y = N-2
            while y >= 0 :
                if board[x][y] != 0 :
                    y2 = y
                    for k in range(y2+1,N) :
                        if board[x][k] == 0 :
                            board[x][k], board[x][y2] = board[x][y2], board[x][k]
                            visited[x][k], visited[x][y2] = visited[x][y2], visited[x][k]
                        elif board[x][k] == board[x][y2] and visited[x][k] == False and visited[x][y2] == False:
                            board[x][k] = board[x][k]*2
                            board[x][y2] = 0
                            visited[x][k] = True
                        else :
                            break
                        y2 = k
                y -= 1
        return max(
                moveBottom(N, copy.deepcopy(board), depth+1),
                moveTop(N, copy.deepcopy(board), depth+1),
                moveRight(N, copy.deepcopy(board),depth+1),
                moveLeft(N, copy.deepcopy(board), depth+1)
                )
                
def moveTop(N, board, depth) :
    if depth == 5 :
        return getMax(N, copy.deepcopy(board))
    else :
        visited = [[False]*N for _ in range(N)]
        for y in range(N) :
            x = 1
            while x < N :
                x2 = x
                for k in range(x2-1,-1,-1) :
                    if board[k][y] == 0 :
                        board[k][y], board[x2][y] = board[x2][y], board[k][y]
                        visited[k][y], visited[x2][y] = visited[x2][y], visited[k][y]
                    elif board[k][y] == board[x2][y] and visited[k][y] == False and visited[x2][y] == False :
                        board[k][y] = board[k][y]*2
                        board[x2][y] = 0
                        visited[k][y] = True
                    else :
                        break
                    x2 = k
                x += 1
        return max(
                moveBottom(N, copy.deepcopy(board), depth+1),
                moveTop(N, copy.deepcopy(board), depth+1),
                moveRight(N, copy.deepcopy(board),depth+1),
                moveLeft(N, copy.deepcopy(board), depth+1)
                )

def moveBottom(N, board, depth) :
    if depth == 5 :
        return getMax(N, copy.deepcopy(board))
    else :
        visited = [[False]*N for _ in range(N)]
        for y in range(N) :
            x = N-2
            while x >= 0 :
                x2 = x
                for k in range(x2+1,N) :
                    if board[k][y] == 0 :
                        board[k][y], board[x2][y] = board[x2][y], board[k][y]
                        visited[k][y], visited[x2][y] = visited[x2][y], visited[k][y]
                    elif board[k][y] == board[x2][y] and visited[k][y] == False and visited[x2][y] == False :
                        board[k][y] = board[k][y]*2
                        board[x2][y] = 0
                        visited[k][y] = True
                    else :
                        break
                    x2 = k
                x -= 1
        return max(
                moveBottom(N, copy.deepcopy(board), depth+1),
                moveTop(N, copy.deepcopy(board), depth+1),
                moveRight(N, copy.deepcopy(board),depth+1),
                moveLeft(N, copy.deepcopy(board), depth+1)
                )

def getMax(N, board) :
    maxV = 0
    for x in range(N) :
        maxV = max(maxV,max(board[x]))
    return maxV

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
print(max(moveBottom(N, copy.deepcopy(board), 0),moveTop(N, copy.deepcopy(board), 0),moveRight(N, copy.deepcopy(board), 0),moveLeft(N, copy.deepcopy(board), 0)))

"""
7
2 2 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 2 2 0 2 2 2 
2 2 2 2 2 2 0
2 2 2 2 2 2 0

답 : 32

10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

답 : 1024
"""