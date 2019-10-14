"""
활주로건설
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
def vertical(n) :
    global N, X
    before, mius, plus = board[0][n], 0, 0
    for i in range(N) :
        if board[i][n] == before :
            if mius :
                mius -= 1
            else :
                plus += 1
        elif mius == 0 and abs(board[i][n]-before) == 1:
            # 이전값보다 큰 경우
            if board[i][n] > before :
                if plus >= X :
                    plus = 1
                    before = board[i][n]
                else :
                    return False
            # 이전값보다 작은 경우
            else :
                plus = 0
                mius = X-1
                before = board[i][n]
        # 다 채워지지 않은 mius가 있다면
        else : 
            return False
    if mius :
        return False
    return True

def horizontal(n) :
    global N, X
    before, mius, plus = board[n][0], 0, 0
    for i in range(N) :
        if board[n][i] == before :
            if mius :
                mius -= 1
            else :
                plus += 1
        elif mius == 0 and abs(board[n][i]-before) == 1 :
            # 이전값보다 큰 경우
            if board[n][i] > before :
                if plus >= X :
                    plus = 1
                    before = board[n][i]
                else :
                    return False
            # 이전값보다 작은 경우
            else :
                plus = 0
                mius = X-1
                before = board[n][i]
        # 다 채워지지 않은 mius가 있다면, 차이가 2 이상인 경우
        else : 
            return False
    if mius :
        return False
    return True


T = int(input())
for test_case in range(1,T+1) :
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N) :
        result += (vertical(i) + horizontal(i))
    print('#{} {}'.format(test_case, result))


"""
1
10 2
2 2 3 5 3 1 1 1 1 1 
2 2 3 5 3 1 1 1 1 1 
3 3 4 5 4 3 2 1 1 2 
3 3 4 5 4 3 2 1 1 2 
5 5 5 5 5 5 3 1 1 3 
4 4 4 5 5 5 4 3 3 3 
4 4 4 5 5 5 5 5 5 3 
4 4 4 4 4 5 5 5 5 3 
4 4 4 4 4 5 5 5 5 3 
5 5 4 4 4 5 5 5 5 4 


"""