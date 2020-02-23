def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    
    while moves :
        y = moves.pop(0)-1

        # 인형 뽑기
        for x in range(N) :
            if board[x][y] :
                # 스택이 비어있지 않고 제일 마지막 인형이 같다면
                if stack and stack[-1] == board[x][y] :
                    stack.pop()
                    answer += 2
                else :
                    stack.append(board[x][y])
                
                board[x][y] = 0
                break
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))