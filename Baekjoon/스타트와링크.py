"""
스타트와 링크
https://www.acmicpc.net/problem/14889
"""
result = 2000

def makeTeam(N, depth, k) :
    if depth == N/2 :
        global result
        A, B = 0, 0
        for x in range(N) :
            for y in range(x+1, N) :
                if visited[x] == visited[y] and visited[x] == 1 :
                    A += board[x][y] + board[y][x]
                elif visited[x] == visited[y] and visited[x] == 0 :
                    B += board[x][y] + board[y][x]
        
        A_B = (A-B) if A > B else (B-A)
        result = min(result, A_B)
    else :
        for i in range(k,N) :
            visited[i] = 1
            makeTeam(N, depth+1, i+1)
            visited[i] = 0


N = int(input())
visited = [0]*N
board = [ list(map(int, input().split())) for _ in range(N)]

# 반만 선택이 되면 됨
visited[0] = 1
makeTeam(N, 1, 1)

print(result)