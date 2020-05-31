"""
주사위 윷놀이
https://www.acmicpc.net/problem/17825
"""

def move_marker(m, score) :
    if m == M :
        global max_sxore
        max_sxore = max(max_sxore, score)
    else :
        for i in range(4) :
            # [1] 도착지점에 있는 값 제외
            if markers[i] == [5,1,0] :
                continue

            # [2] 시작 위치가 같은 애들 제외
            same_position = False
            for j in range(i) :
                if markers[i] == markers[j] :
                    same_position = True
                    break
            if same_position :
                continue
            
            # [3] 이동
            x, y, v = markers[i]
            for _ in range(move[m]) :
                y += 1
                if y == len(score_board[x]) :
                    if x == 0 or x == 4:
                        y = 0
                        x = 5
                    elif x < 4 :
                        y = 0
                        x = 4
                    else :
                        # 도착!
                        v = 0
                        break
                v = score_board[x][y]
            # 마지막 칸이 파란색인 경우
            if x == 0 :
                if v == 10 :
                    x, y = 1, -1
                elif v == 20 :
                    x, y = 2, -1
                elif v == 30 :
                    x, y =  3, -1

            # [4] 이동을 마치는 칸에 다른 값이 존재하지 않는다면 이동 가능
            can_move = True
            # 단, 도착지점일 경우에는 중복 가능
            if v != 0 :
                for j in range(4) :
                    if i == j :
                        continue
                    if markers[j] == [x,y,v] :
                        can_move = False
                        break
            if can_move :
                x, y, v, markers[i] = markers[i][0], markers[i][1], markers[i][2], [x, y, v]
                move_marker(m+1, score+markers[i][2])
                markers[i] = [x, y, v]


score_board = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
    [13, 16, 19],
    [22, 24],
    [28, 27, 26],
    [25, 30, 35],
    [40]
]

move = list(map(int, input().split()))
M = len(move)

max_sxore = 0
markers = [[0, 0, 0] for _ in range(4)]
move_marker(0, 0) 
print(max_sxore)