"""
Puyo Puyo
https://www.acmicpc.net/problem/11559
"""
def isNotWall(x,y) :
    if x < 0 or x >= 12 :
        return False
    if y < 0 or y >= 6 :
        return False
    return True

def PuyoDown():
    for x in range(10,-1,-1) :
        for y in range(6) :
            if board[x][y] != "." :
                a = x
                while a+1 < 12 :
                    if board[a+1][y] == "." :
                        board[a+1][y], board[a][y] = board[a][y], board[a+1][y]
                        a = a+1
                    else : 
                        break
    # for x in range(12) :
    #     print(board[x])
    # print("==========")
    PuyoCheck()


# 4개 이상 상하좌우 연결 체크
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def PuyoCheck() :
    visited = [[False]*6 for _ in range(12)]
    cascade = False
    for x in range(11,-1,-1) :
        for y in range(6) :
            # 뿌요 찾기
            Puyo = []
            if board[x][y] != "." and visited[x][y] == False :
                visited[x][y] = True

                queue =[[x,y]]
                while queue :
                    a, b = queue.pop(0)
                    Puyo.append([a,b])

                    for i in range(4) :
                        # 벽이 아니고 지나간 적이 없으며, 나와 같은 값이라면 추가!
                        if isNotWall(a+dx[i],b+dy[i]) and visited[a+dx[i]][b+dy[i]] == False and board[a+dx[i]][b+dy[i]]== board[a][b] :
                            visited[a+dx[i]][b+dy[i]] = True
                            queue.append([a+dx[i],b+dy[i]])

                if len(Puyo) >= 4 :
                    # 연쇄반응 추가
                    cascade = True
                    # 터트리기
                    while Puyo :
                        a, b = Puyo.pop(0)
                        board[a][b] = "."
    if cascade :
        global result
        result += 1
        # 내려보내기
        PuyoDown()

        
result = 0
board = [ " ".join(input()).split() for _ in range(12) ]
PuyoCheck()

print(result)
