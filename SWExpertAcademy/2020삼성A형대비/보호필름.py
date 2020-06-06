"""
보호필름
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
def pass_test() :
    for y in range(W) :
        is_pass, X, cnt = False, board[0][y], 1
        for x in range(1, D):
            if X == board[x][y] :
                cnt += 1
            else :
                X = board[x][y]
                cnt = 1
            if cnt >= K :
                is_pass = True
                break
        if not is_pass :
            return False
    return True

def drop_reagent(cnt, k) :
    global drop_count
    if cnt < drop_count :
        # [1] 시약 검사
        if pass_test() :
            drop_count = cnt
        # [2] 약품 치기
        else :
            for i in range(k, D) :
                temp = board[i]
                board[i] = [0]*W
                drop_reagent(cnt+1, i+1)
                board[i] = [1]*W
                drop_reagent(cnt+1, i+1)
                board[i] = temp

T = int(input())
for test_case in range(1, 1+T) :
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    drop_count = D
    drop_reagent(0, 0)
    print('#{} {}'.format(test_case, drop_count))

"""

1   
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
"""