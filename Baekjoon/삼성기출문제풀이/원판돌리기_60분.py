"""
원판돌리기
https://www.acmicpc.net/problem/17822
"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

def clockwise(x,k) :
    while k :
        temp = board[x][-1]
        for y in range(M) :
            board[x][y], temp = temp, board[x][y]
        k -= 1

def counterclockwise(x, k):
    while k:
        temp = board[x][0]
        for y in range(M-1,-1,-1):
            board[x][y], temp = temp, board[x][y]
        k -= 1

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for _ in range(T) :
    x, d, k = map(int, input().split())
    # [1] x의 배수를 d방향으로 k번 회전
    for i in range(x, N+1, x) :
        if d :
            counterclockwise(i-1,k)
        else :
            clockwise(i-1,k)

    # [2] 원판에 남은 수 확인 + 평균 구하기
    is_removed, num_sum, num_cnt = False, 0, 0
    visited = [[False]*M for _ in range(N)]
    for x in range(N) :
        for y in range(M) :
            if board[x][y] and not visited[x][y]:
                visited[x][y] = True
                queue = [[x,y]]
                is_remove = False
                while queue :
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if is_not_wall(a+dx[i], (b+dy[i])%M) and not visited[a+dx[i]][(b+dy[i])%M] and board[a+dx[i]][(b+dy[i])%M] == board[x][y] :
                            visited[a+dx[i]][(b+dy[i])%M] = True
                            queue.append([a+dx[i],(b+dy[i])%M])
                            board[a+dx[i]][(b+dy[i])%M] = 0
                            is_remove = True
                            is_removed = True
                if is_remove :
                    board[x][y] = 0
                else :
                    num_cnt += 1
                    num_sum += board[x][y]

    if not is_removed and num_cnt :
        num_avg = num_sum/num_cnt
        for x in range(N) :
            for y in range(M) :
                if board[x][y] :
                    if board[x][y] > num_avg :
                        board[x][y] -= 1
                    elif board[x][y] < num_avg :
                        board[x][y] += 1

result = 0
for x in range(N) :
    for y in range(M):
        result += board[x][y]

print(result)



