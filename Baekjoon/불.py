"""
불
https://www.acmicpc.net/problem/5427
"""
# import sys
# sys.stdin = open('input.txt','r')
import collections

def isNotWall(N,M,x,y) :
    if x >= 0 and x < N :
        if y >= 0 and y < M :
            if arr[x][y] != '#' :
                return True
    return False

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def moveFire(N,M,fire) :
    nextFire = collections.deque([])
    l, L = 0, len(fire)
    while l < L :
        q = fire[l]
        x, y = q[0], q[1] 
        for i in range(4) :
            if isNotWall(N,M,x+dx[i],y+dy[i]) and arr[x+dx[i]][y+dy[i]] == '.':
                arr[x+dx[i]][y+dy[i]] = '*'
                nextFire.append([x+dx[i],y+dy[i]])
        l += 1
    return nextFire

def findExit(N,M,x,y,fire) :
    queue = collections.deque([])
    queue.append([x,y,0,0])
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    beforeF = -1
    while queue :
        q = queue.popleft()
        x,y,depth, f = q[0], q[1], q[2], q[3]
        # if visited[x][y] == False :
        
        # 현재 위치가 출구라면?
        if arr[x][y] == '.' and (x == 0 or x == N-1 or y == 0 or y == M-1) :
            return depth+1
        if f != beforeF :
            beforeF = f
            fire = moveFire(N,M,fire)
        for i in range(4) :
            if isNotWall(N,M,x+dx[i],y+dy[i]) and arr[x+dx[i]][y+dy[i]] == '.' and visited[x+dx[i]][y+dy[i]] == False:
                visited[x+dx[i]][y+dy[i]] = True
                queue.append([x+dx[i],y+dy[i],depth+1,f+1])

    return 'IMPOSSIBLE'

T = int(input())
for test_case in range(T) :
    M, N = map(int, input().split())
    arr = [list(" ".join(input().split())) for _ in range(N)]
    
    startX, startY = 0, 0
    fire = collections.deque([])
    for x in range(N) :
        for y in range(M) :
            if arr[x][y] == '*' :
                fire.append([x,y])
            elif arr[x][y] == '@' :
                arr[x][y] = '.'
                startX, startY = x, y
    
    print(findExit(N,M,startX,startY,fire))

"""
21
1 1
@
3 3
.#.
#@#
.#.
3 3
...
.@.
...
3 3
.#.
#@#
.#*
8 3
########
#*@.....
########
5 6
##.##
#...#
#.#.#
#.#@#
#*#.#
#####
5 6
##.##
#...#
#.#.#
#*#@#
#.#.#
#####
5 6
##.##
#...#
#*#.#
#.#@#
#.#.#
#####
8 9
########
#......#
#.####.#
#.#@.#.#
#.##.#.#
#....#.#
######.#
.......#
########
5 3
##.##
#*.@#
#####
7 7
.......
.*#.##.
.##.##.
...@...
.##.##.
.##.#*.
.......
7 7
......*
.##.##.
.##.##.
...@...
.##.##.
.##.##.
*......
7 7
.*....*
.##.##.
.##.##.
...@...
.##.##.
.##.##.
.*....*
7 7
.......
*##.##*
.##.##.
...@...
.##.##.
.##.##.
*.....*
7 7
*....*.
.##.##.
.##.##.
...@...
.##.##.
.##.##.
*....*.
7 7
*.....*
.##.##.
.##.##.
...@...
.##.##.
*##.##*
.......
7 7
..#.#..
.*#.#*.
.##.##.
...@...
.##.##.
.*#.#*.
.......
7 7
.......
.*#.#*.
.##.###
...@...
.##.###
.*#.#*.
.......
7 7
.......
.*#.#*.
###.##.
...@...
###.##.
.*#.#*.
.......
7 7
.......
.*#.#*.
.##.##.
...@...
.##.##.
.*#.#*.
..#.#..
5 3
..#..
.@#*.
..#..
"""