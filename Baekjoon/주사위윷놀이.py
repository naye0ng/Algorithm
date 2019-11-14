"""
주사위 윷놀이 
https://www.acmicpc.net/problem/17825
"""

jump = [2,3,2,-1,5]
def moveAndGetScore(L,l, score, points) :
    if L == l :
        global maxScore
        maxScore = max(maxScore, score)
    else :
        for i in range(4) :
            if points[i][0] <= 40 :
                tmp = points[i]
                point, d = points[i]
                for _ in range(move[l]) :
                    point += jump[d]
                    if d == 1 and point > 19 :
                        d = 4
                        point = 25
                    elif d == 2 and point > 25 :
                        d = 4
                        point = 25
                    elif d == 3 and point == 25 :
                        d = 4
                        point = 25
                    elif point > 40 :
                        break
                
                jumpOk = True
                if point == 10 :
                    if d == 0:
                        d = 1
                    for k in range(4) :
                        if points[k][0] == point :
                            jumpOk = False
                            break
                elif point == 20 :
                    d = 2
                    for k in range(4) :
                        if points[k][0] == point :
                            jumpOk = False
                            break
                elif point == 30 :
                    if d == 0:
                        d = 3
                    for k in range(4) :
                        if points[k][0] == point :
                            jumpOk = False
                            break
                elif point == 40 :
                    for k in range(4) :
                        if points[k][0] == point :
                            jumpOk = False
                            break 
                elif point < 40 :
                    for k in range(4) :
                        if points[k][0] == point and points[k][1] == d :
                            jumpOk = False
                            break 
                
                if jumpOk :
                    points[i] = [point,d]
                    if point <= 40 :
                        moveAndGetScore(L,l+1, score+point, points)
                    else :
                        moveAndGetScore(L,l+1, score, points)
                    points[i] = tmp


move = list(map(int, input().split()))
L = len(move)
maxScore = 0

moveAndGetScore(L,0, 0, [[0,0] for _ in range(4)])
print(maxScore)

