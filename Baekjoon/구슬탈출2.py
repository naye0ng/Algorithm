"""
구슬탈출2
https://www.acmicpc.net/problem/13460
"""

def right(N,M,puzzle) :
    i = 1
    b, r = False, False 
    while(i <= N-2) :
        for j in range(1,M-2) :
            if puzzle[i][j] == 'R' and puzzle[i][j+1] == '.' :
                puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]
                r = True
            elif puzzle[i][j] == 'B' and puzzle[i][j+1] == '.' :
                puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]
                b = True
            elif puzzle[i][j] == 'R' and puzzle[i][j+1] == 'B' and puzzle[i][j+2] == '.':
                puzzle[i][j] = '.'
                puzzle[i][j+1] = 'R'
                puzzle[i][j+2] = 'B'
                b, r = True, True 
            elif puzzle[i][j] == 'B' and puzzle[i][j+1] == 'R' and puzzle[i][j+2] == '.':
                puzzle[i][j] = '.'
                puzzle[i][j+1] = 'B'
                puzzle[i][j+2] = 'R'
                b, r = True, True 
        i += 1
        if b and r :
            break

def left(N,M,puzzle) :
    i = 1
    b, r = False, False 
    while(i <= N-2) :
        for j in range(M-2,0,-1) :
            if puzzle[i][j] == 'R' and puzzle[i][j-1] == '.' :
                puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]
                r = True
            elif puzzle[i][j] == 'B' and puzzle[i][j-1] == '.' :
                puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]
                b = True
            elif puzzle[i][j] == 'R' and puzzle[i][j-1] == 'B' and puzzle[i][j-2] == '.':
                puzzle[i][j] = '.'
                puzzle[i][j-1] = 'R'
                puzzle[i][j-2] = 'B'
                b, r = True, True 
            elif puzzle[i][j] == 'B' and puzzle[i][j-1] == 'R' and puzzle[i][j-2] == '.':
                puzzle[i][j] = '.'
                puzzle[i][j-1] = 'B'
                puzzle[i][j-2] = 'R'
                b, r = True, True 
        i += 1
        if b and r :
            break

def top(N,M,puzzle) :
    pass

def bottom(N,M,puzzle) :
    pass

# 세로, 가로
N, M = map(int, input().split())
puzzle = [" ".join(input()).split() for _ in range(N)]

left(N,M,puzzle)
right(M,N,puzzle)

"""
7 7
#######
#.R..B#
#.#####
#.....#
#####.#
#..R..#
#######
"""