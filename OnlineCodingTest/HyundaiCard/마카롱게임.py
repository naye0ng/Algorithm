dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_not_wall(x, y) :
    if x < 0 or x >= 6 :
        return False
    if y < 0 or y >= 6 :
        return False
    return True

def bomb() :
    is_bomb = False
    visited = [[False]*6 for _ in range(6)]
    for x in range(6) :
        for y in range(6) :
            if board[x][y] and not visited[x][y] :
                queue = []
                queue.append([x,y])
                visited[x][y] = True
                q = 0
                while q < len(queue) :
                    a, b = queue[q]
                    for i in range(4) :
                        if is_not_wall(a+dx[i], b+dy[i]) and not visited[a+dx[i]][b+dy[i]] and board[a][b] == board[a+dx[i]][b+dy[i]] :
                            queue.append([a+dx[i], b+dy[i]])
                            visited[a+dx[i]][b+dy[i]] = True
                    q += 1
                if q >= 3 :
                    is_bomb = True
                    for i in range(q) :
                        board[queue[i][0]][queue[i][1]] = 0
    # 하나라도 터졌다면 True
    return is_bomb

board = [[0]*6 for _ in range(6)]
def solution(macaron):
    height = [5]*6
    for L, C in macaron :
        board[height[L-1]][L-1] = C
        height[L-1] -= 1
        # 마카롱을 터트린다.
        while bomb() :
            # 원상복구
            for y in range(6) :
                for x in range(5,-1,-1) :
                    if board[x][y] == 0 :
                        # 가장 가까운 마카롱으로 바꾸기
                        for k in range(x-1,-1,-1) :
                            if board[k][y] != 0 :
                                board[x][y], board[k][y] = board[k][y], board[x][y] 
                                break
                for x in range(6) :
                    if board[x][y] != 0 :
                        height[y] = x-1
                        break
    answer = [""]*6
    for i in range(6) :
        answer[i] = "".join(map(str,board[i]))
    return answer

print(solution([[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]))