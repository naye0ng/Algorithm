# 테트리스
import copy
global answer, col, row

# 빈칸의 개수 계산
def emptyNum(board) :
    n = len(board)
    global col, row
    col = [0]*n
    row = [0]*n
    
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 0 :
                col[i] += 1
                row[j] += 1
# 가득 차있는 값 고르기
def findFull(board) :
    count = 0
    for b in board :
        if sum(b) == len(b) :
            count +=1 
    return count

def block00(board) :
    global row, answer
    answer = 0
    for i in range(len(row)) :
        if row[i] >= 3 :
            copy_board = copy.deepcopy(board)
            # 해당 행 채우기
            copy_board[row[i]-1][i] = 1
            copy_board[row[i]-2][i] = 1
            copy_board[row[i]-3][i] = 1
            count = findFull(copy_board)
            if answer == 0 or answer < count :
                answer = count

def block01(board) :
    global col, answer
    answer = 0
    for i in range(len(col)) :
        if col[i] >= 3 :
            copy_board = copy.deepcopy(board)
            copy_board[i][col[i]]




def solution(block, board):
    # 초기화
    emptyNum(board)
    if block == 0 :
        block00(board)

    return answer

print(solution(0,[[1,0,0,0],[1,0,0,1],[1,1,0,1],[1,1,0,1]]))