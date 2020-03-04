"""
스도쿠
https://www.acmicpc.net/problem/2580
"""
def can_be_answer(x, y, n) :
    # 가로, 세로에 n이 존재하면 안됨
    for i in range(9) :
        if board[x][i] == n or board[i][y] == n:
            return False
    
    # 달팽이 모양 체크
    for i in range((x//3)*3, (x//3)*3+3) :
        for j in range((y//3)*3, (y//3)*3+3) :
            if board[i][j] == n :
                return False
    return True

is_not_end = True
def DFS(x, y, k) :
    global is_not_end
    if k == len(empty) :
        is_not_end = False
        for i in range(9) :
            print(" ".join(map(str,board[i])))
    elif is_not_end :
        for i in range(1,10) :
            if number[i] >= 1 and can_be_answer(empty[k][0], empty[k][1], i) :
                number[i] -= 1
                board[empty[k][0]][empty[k][1]] = i
                # k는 empty의 index로 다음 칸의 정보를 담고 있다.
                DFS(empty[k][0], empty[k][1], k+1) 
                board[empty[k][0]][empty[k][1]] = 0
                number[i] += 1

board = [ list(map(int, input().split())) for _ in range(9)]
number = { n:9 for n in range(1,10)}

empty = []
for x in range(9) :
    for y in range(9) :
        if board[x][y] == 0:
            empty.append([x,y])
        else :
            number[board[x][y]] -= 1

DFS(0, 0, 0)