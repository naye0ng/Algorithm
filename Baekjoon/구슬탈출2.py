"""
구슬탈출2
https://www.acmicpc.net/problem/13460

TIP : 왼쪽으로 이동한 후에는 왼쪽, 오른쪽으로 이동하지 않아도 된다.
"""
import copy

global result
result = 100

def moveLeft(N,M,arr,depth) :
    global result
    if depth <= 10 and depth < result :
        puzzle = copy.deepcopy(arr)
        x = 1
        y = 1
        count = 0
        R = False
        isNotEnd = True
        while x <= N-2 and count < 2 and isNotEnd:
            while y <= M-2 and count < 2 and isNotEnd:
                if puzzle[x][y] == 'R' or puzzle[x][y] == 'B' :
                    k = y 
                    while k >= 1 :
                        if puzzle[x][k-1] == '.' :
                            puzzle[x][k], puzzle[x][k-1] = puzzle[x][k-1], puzzle[x][k]
                        elif puzzle[x][k-1] == 'O' :
                            if puzzle[x][k] == 'B' :
                                isNotEnd = False
                            else :
                                puzzle[x][k] = '.'
                                R = True
                            break
                        else :
                            break
                        k -= 1
                y += 1
            y = 1
            x += 1
        if isNotEnd :
            if R :
                result = depth
            else : 
                moveTop(N,M,puzzle,depth+1)
                moveBottom(N,M,puzzle,depth+1)

def moveRight(N,M,arr,depth) :
    global result
    if depth <= 10 and depth < result :
        puzzle = copy.deepcopy(arr)
        x = 1
        y = M-2
        count = 0
        R = False
        isNotEnd = True
        while x <= N-2 and count < 2 and isNotEnd:
            while y >= 1 and count < 2 and isNotEnd:
                if puzzle[x][y] == 'R' or puzzle[x][y] == 'B' :
                    count += 1
                    k = y
                    while k <= M-2 :
                        if puzzle[x][k+1] == '.' :
                            puzzle[x][k], puzzle[x][k+1] = puzzle[x][k+1], puzzle[x][k]
                        elif puzzle[x][k+1] == 'O' :
                            if puzzle[x][k] == 'B' :
                                isNotEnd = False
                            else :
                                puzzle[x][k] = '.'
                                R = True
                            break
                        else :
                            break
                        k += 1
                y -= 1
            y = M-2
            x += 1
        if isNotEnd :
            if R :
                result = depth
            else : 
                moveTop(N,M,puzzle,depth+1) 
                moveBottom(N,M,puzzle,depth+1)

def moveTop(N,M,arr,depth) :
    global result
    if depth <= 10 and depth < result :
        puzzle = copy.deepcopy(arr)
        x = 1
        y = 1
        count = 0
        R = False
        isNotEnd = True
        while y <= M-2 and count < 2 and isNotEnd:
            while x <= N-2 and count < 2 and isNotEnd:
                if puzzle[x][y] == 'R' or puzzle[x][y] == 'B' :
                    k = x 
                    while k >= 1 :
                        if puzzle[k-1][y] == '.' :
                            puzzle[k][y], puzzle[k-1][y] = puzzle[k-1][y], puzzle[k][y] 
                        elif puzzle[k-1][y] == 'O' :
                            if puzzle[k][y] == 'B' :
                                isNotEnd = False
                            else :
                                puzzle[k][y] = '.'
                                R = True 
                            break
                        else :
                            break
                        k -= 1
                x += 1 
            x = 1
            y += 1
        if isNotEnd :
            if R :
                result = depth
            else : 
                moveRight(N,M,puzzle,depth+1)
                moveLeft(N,M,puzzle,depth+1) 

def moveBottom(N,M,arr,depth) :
    global result
    if depth <= 10 and depth < result :
        puzzle = copy.deepcopy(arr)
        x = N-2
        y = 1
        count = 0
        R = False
        isNotEnd = True
        while y <= M-2 and count < 2 and isNotEnd:
            while x >= 1 and count < 2 and isNotEnd:
                if puzzle[x][y] == 'R' or puzzle[x][y] == 'B' :
                    k = x 
                    while k <= N-2 :
                        if puzzle[k+1][y] == '.' :
                            puzzle[k][y], puzzle[k+1][y] = puzzle[k+1][y], puzzle[k][y] 
                        elif puzzle[k+1][y] == 'O' :
                            if puzzle[k][y] == 'B' :
                                isNotEnd = False
                            else :
                                puzzle[k][y] = '.'
                                R = True 
                            break
                        else :
                            break
                        k += 1
                x -= 1 
            x = N-2
            y += 1
        if isNotEnd :
            if R :
                result = depth
            else : 
                moveRight(N,M,puzzle,depth+1)
                moveLeft(N,M,puzzle,depth+1) 


N, M = map(int, input().split())
arr = [" ".join(input()).split() for _ in range(N)]

moveRight(N,M,arr,1)
moveLeft(N,M,arr,1) 
moveTop(N,M,arr,1) 
moveBottom(N,M,arr,1) 
if result == 100 :
    result = -1
print(result)