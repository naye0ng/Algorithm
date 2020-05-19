"""
원판돌리기
https://www.acmicpc.net/problem/17822
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def clockwise(x, k) :
    for _ in range(k) :
        temp = board[x][-1]
        for y in range(M) :
            board[x][y], temp = temp, board[x][y]

def counterclockwise(x, k) :
    for _ in range(k) :
        temp = board[x][0]
        for y in range(M-1,-1,-1) :
            board[x][y], temp = temp, board[x][y]

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T) :
    x, d, k = map(int, input().split())

    # 회전
    for i in range(1, N//x+1) :
        if d :
            counterclockwise((x*i)-1, k)
        else :
            clockwise((x*i)-1, k)
    """
    조건을 꼼꼼히 읽어보자!
    """
    # 2-1. 인접한 수 찾아서 지우기
    is_not_removed = True
    visited = [[False]*M for _ in range(N)]
    total, num = 0, 0
    for x in range(N) :
        for y in range(M) :
            if board[x][y] :
                visited[x][y] = True
                queue = [[x,y]]
                is_same = False
                while queue :
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if 0 <= a+dx[i] < N and not visited[a+dx[i]][(b+dy[i])%M] and board[x][y] == board[a+dx[i]][(b+dy[i])%M] :
                            is_same = True
                            board[a+dx[i]][(b+dy[i])%M] = 0
                            queue.append([a+dx[i], (b+dy[i])%M])
                            visited[a+dx[i]][(b+dy[i])%M] = True
                if is_same :
                    board[x][y] = 0
                    is_not_removed = False
                else :
                    total += board[x][y]
                    num += 1
    
    # 2-2. 지워진 값 없다면 +1, -1 처리
    if is_not_removed :
        """
        [런타임에러 주의]
        나누기를 할 때, 0으로 나눠지는 경우를 항상 예외처리하자!!
        """
        if num > 0 :
            avg = total/num
            for x in range(N) :
                for y in range(M) :
                    if board[x][y] :
                        if board[x][y] < avg :
                            board[x][y] += 1
                        elif board[x][y] > avg :
                            board[x][y] -= 1
# 원판에 적힌 수의 합
result = 0
for x in range(N) :
    for y in range(M) :
        result += board[x][y]

print(result)

                


    
