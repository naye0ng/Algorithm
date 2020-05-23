import copy

def drop_and_bomb(score, board) :
    is_not_end = True
    while is_not_end :
        # [1] 빈칸 채우기
        for y in range(N) :
            for x in range(N-1,-1,-1) :
                if board[x][y] == 0 :
                    # 가장 가까운 사탕 찾기
                    for k in range(x-1,-1,-1) :
                        if board[k][y] != 0 :
                            board[x][y], board[k][y] = board[k][y], board[x][y]
                            break

        # [2] 사탕덩어리 찾기
        remove = set()
        for k in range(N) :
            length = 0
            x = 0
            while x < N-1 :
                if board[x][k] != 0 and board[x][k] == board[x+1][k] :
                    length += 1

                if board[x][k] != board[x+1][k] and length > 0 :
                    if length >= 2 :
                        for i in range(length+1) :
                            remove.add((x-i,k))
                    length = 0
                x += 1
            if length >= 2 :
                for i in range(length+1) :
                    remove.add((x-i,k))

            length = 0
            y = 0
            while y < N-1 :
                if board[k][y] != 0 and board[k][y] == board[k][y+1] :
                    length += 1

                if board[k][y] != board[k][y+1] and length > 0 :
                    if length >= 2 :
                        for i in range(length+1) :
                            remove.add((k, y-i))
                    length = 0
                y += 1
            if length >= 2 :
                for i in range(length+1) :
                    remove.add((k, y-i))


        if len(remove) > 0 :
            score += len(remove)
            for x, y in remove :
                board[x][y] = 0
        else :
            # 제거된 것이 없다면 끝
            is_not_end = False
            global maxScore
            maxScore = max(maxScore, score)


N, maxScore = 0, 0
def solution(board):
    global N, maxScore
    N = len(board)

    for x in range(N) :
        for y in range(N) :
            temp, board[x][y] = board[x][y], 0
            drop_and_bomb(1, copy.deepcopy(board))
            board[x][y] = temp

    return maxScore