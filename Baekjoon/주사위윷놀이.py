"""
주사위 윷놀이
https://www.acmicpc.net/problem/17825
"""
maxScore = 0
# 이동가능 : 겹치면 안됨
def is_ok(i,x,y,l) :
    for j in range(4) :
        if j == i : continue
        # 일단 x,y가 같음 아웃 : 30이 두 개 있는거 주의
        if point[j][0] == x and point[j][1] == y : return False
    return True

def move(score, n, path) :
    if n == 10 :
        global maxScore
        maxScore = max(maxScore, score)
        # print(path, score)
    else :
        # point[i]번째 말을 number[n]만큼 이동
        for i in range(4) :
            # [1] 이동이 가능하고,
            x,y,l = point[i]
            if x < len(board) :
                y += number[n]
                if x == 0 :
                    if y < len(board[x]) :
                        if board[x][y] in [10,20,30] :
                            x = board[x][y] // 10
                            y = -1
                    elif y >= len(board[x]) and y < (len(board[x]) + len(board[5])):
                        # 5번째 줄로 넘어감
                        x = 5 
                        y = 0
                    elif y >= (len(board[x]) + len(board[5])) :
                        # 나가리
                        x = len(board)
                        
                elif x in [1,2,3] :
                    if y >= len(board[x]) and y < (len(board[x]) + len(board[4])):
                        # 4번째 줄로 넘어감
                        y -= len(board[x])
                        x = 4
                    elif y >= (len(board[x]) + len(board[4])) and y < (len(board[x]) + len(board[4]) + len(board[5])):
                        # 5번째 줄로 넘어감
                        x = 5 
                        y = 0
                    elif y >= (len(board[x]) + len(board[4]) + len(board[5])) :
                        # 나가리
                        x = len(board)
                elif x == 4 :
                    if y >= len(board[x]) and y < (len(board[x]) + len(board[5])):
                        # 5번째 줄로 넘어감
                        x = 5 
                        y = 0
                    elif y >= (len(board[x]) + len(board[5])) :
                        # 나가리
                        x = len(board)
                else :
                    # 무조건 나가리
                    x = len(board)
                # [2] 이동하려는 곳이 나가리거나 아무것도 없다면 => 이동하기
                if x == len(board) :
                    before_p, point[i] = point[i], [x,y,0]
                    move(score, n+1, path + [[i,0]]) 
                    point[i] = before_p
                elif x < len(board) :
                    l = board[x][y]
                    if y == -1 : 
                        if x <= 3 and x > 0:
                            l = x*10
                        else :
                            print(x,y,"이거므ㅏ임")
                    if is_ok(i,x,y,l) : 
                        # -1로 쓴 y값이 문제였을 듯 
                        before_p, point[i] = point[i], [x,y,l]
                        move(score+l, n+1, path + [[i,l]]) 
                        point[i] = before_p
                   

number = list(map(int, input().split()))
board = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
    [13, 16, 19], 
    [22, 24],
    [28, 27, 26],
    [25, 30, 35],
    [40]
]

point = [[0,0,0] for _ in range(4)]
move(0, 0,[]) 
print(maxScore)
