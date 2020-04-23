"""
활주로건설
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH
"""
def horizontal(x) :
    h = board[x][0]
    h_cnt = 1
    is_down = False
    for y in range(1,N) :
        if is_down :
            if h == board[x][y] :
                h_cnt += 1
                if h_cnt == X :
                    h_cnt = 0
                    is_down = False
            else :
                return False
        else :
            if h == board[x][y] :
                h_cnt += 1
            elif h > board[x][y] :
                if h-board[x][y] == 1 :
                    h = board[x][y]
                    h_cnt = 1
                    is_down = True
                else :
                    return False
            elif h < board[x][y] :
                if board[x][y]-h == 1 and h_cnt >= X :
                    h = board[x][y]
                    h_cnt = 1
                else :
                    return False
    if is_down :
        return  False
    return True

def vertical(y) :
    h = board[0][y]
    h_cnt = 1
    is_down = False
    for x in range(1, N):
        if is_down:
            if h == board[x][y]:
                h_cnt += 1
                if h_cnt == X:
                    h_cnt = 0
                    is_down = False
            else:
                return False
        else:
            if h == board[x][y]:
                h_cnt += 1
            elif h > board[x][y]:
                if h - board[x][y] == 1:
                    h = board[x][y]
                    h_cnt = 1
                    is_down = True
                else:
                    return False
            elif h < board[x][y]:
                if board[x][y] - h == 1 and h_cnt >= X:
                    h = board[x][y]
                    h_cnt = 1
                else:
                    return False
    if is_down:
        return False
    return True

T = int(input())
for test_case in range(1, 1+T) :
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for n in range(N) :
        result += horizontal(n) + vertical(n)

    print('#{} {}'.format(test_case, result))


"""
1
6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2
"""