
import copy

# 가득 차있는 값 고르기
def findFull(board) :
    count = 0
    for b in board :
        if sum(b) == len(b) :
            count +=1 
    return count

def solution(block, board):
    answer = 0
    if block == 0 :
        dy = [0,0,0]
        dx = [0,-1,-2]
        
    elif block == 1 :
        dy = [0,-1,-2]
        dx = [0,0,0]
    elif block == 2 :
        dy = [0,-1,-1]
        dx = [0,0,-1]
    elif block == 3 :
        dy = [0,0,-1]
        dx = [0,-1,0]
    elif block == 4 :
        dy = [0,0,-1]
        dx = [0,-1,-1]
    elif block == 5 :
        dy = [0,0,1]
        dx = [0,-1,-1]
        
    n = len(board)
    for x in range(n-1,-1,-1) :
        for y in range(n-1,-1,-1) :
            copy_board = copy.deepcopy(board)
            t = 0
            for i in range(3) :
                if x+dx[i] >= n or x+dx[i] < 0 :
                    break
                if y+dy[i] >= n or y+dy[i] < 0 :
                    break
                if copy_board[x+dx[i]][y+dy[i]] == 0 :
                    t += 1
            
            if t == 3 : 
                for i in range(3) :
                    copy_board[x+dx[i]][y+dy[i]] = 1

                count = findFull(copy_board)
                if answer == 0 or answer < count :
                    answer = count
            
    return answer

print(solution(0,[[1,0,0,0],[1,0,0,1],[1,1,0,1],[1,1,0,1]]))