'''
돌려 돌려 돌림판!
https://www.acmicpc.net/problem/11504
'''
def check_number(X, Y, number) :
    if number < X : return 0
    if number > Y : return 0
    return 1


T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    X = int(''.join(input().split()))
    Y = int(''.join(input().split()))
    board = input().split()
    board.extend(board)

    answer = 0
    for i in range(N) :
        answer += check_number(X, Y, int(''.join(board[i:i+M])))
    
    print(answer)

