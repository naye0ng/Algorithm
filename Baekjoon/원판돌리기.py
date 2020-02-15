"""
원판돌리기
https://www.acmicpc.net/problem/17822
"""
# 인접하는 곳
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def find_same_value() :
    is_same = False
    for x in range(N) :
        for y in range(M) :
            if board[x][y] != 0 :
                queue = []
                queue.append([x,y])
                z = board[x][y]
                while queue :
                    a, b = queue.pop(0)
                    for i in range(4) :
                        if (a+dx[i] >= 0 and a+dx[i] < N) and board[a+dx[i]][(b+dy[i])%M] == z:
                            queue.append([a+dx[i],(b+dy[i])%M])
                            board[a+dx[i]][(b+dy[i])%M] = 0
                            # 같은 값이 있다면 (2)번 조건 수행 안함
                            is_same = True

    if not is_same :
        # 원판에 적힌 수의 평균기준으로 평가
        sum_of, num = 0, 0
        for x in range(N) :
            for y in range(M) :
                if board[x][y] != 0 :
                    sum_of += board[x][y]
                    num += 1
        """ 
        [1] 문제를 제대로 읽자! 소수점을 버리라는 말이 없다!!
        [2] sum_of/num는 num이 0 이면 문제생긴다.
        """
        avg = sum_of/num if num != 0 else 0
        
        for x in range(N) :
            for y in range(M) :
                if board[x][y] != 0 :
                    if board[x][y] > avg : board[x][y] -= 1
                    elif board[x][y] < avg : board[x][y] += 1

def one_rotate(x,k) :
    for i in range(N) :
        # 번호가 x의 배수인 원판을 k를 기준으로 회전
        if (i+1) % x == 0 :
            board[i] = board[i][k:] + board[i][:k]  

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T) :
    x, d, k = map(int, input().split())
    if d == 0 : k = M-k
    one_rotate(x,k)
    find_same_value()

print(sum([sum(board[x]) for x in range(N)]))


"""
4 4 1
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
2 0 1
"""