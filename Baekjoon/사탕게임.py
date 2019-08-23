"""
사탕게임
https://www.acmicpc.net/problem/3085
"""
# 가장 긴 사탕 먹기
# def eatCandy(N,changedCandy) :
#     maxCol, maxRow = 1, 1
#     bx, by = 0, 0
#     for x in range(N) :
#         row = 1 
#         bx = x
#         for y in range(N) :
#             if y == 0 :
#                 by = 0
#             elif changedCandy[bx][by] == changedCandy[x][y] :
#                 row += 1
#                 maxRow = max(maxRow,row)
#             else :
#                 row = 1
#             maxRow = max(maxRow,row)  
#             by = y
#     bx, by = 0, 0
#     for x in range(N) :
#         col = 1 
#         bx = x
#         for y in range(N) :
#             if y == 0 :
#                 by = 0
#             elif changedCandy[by][bx] == changedCandy[y][x] :
#                 col += 1
#                 maxCol = max(maxCol,col)
#             else :
#                 col = 1
#             maxCol = max(maxCol,col)  
#             by = y
#     return max(maxCol, maxRow)


# 변경된 줄만 바꾸기

    

# 인접한 사탕 고르기
def changeCandy(N) :
    maxCandy = 0
    for x in range(N) :
        for y in range(N-1) :
            # 왼-오
            if candy[x][y] != candy[x][y+1] :
                candy[x][y], candy[x][y+1] = candy[x][y+1], candy[x][y]
                maxCandy = max(maxCandy, eatCandy(N,candy))
                candy[x][y], candy[x][y+1] = candy[x][y+1], candy[x][y]
            # 위-아래
            if candy[y][x] != candy[y+1][x] :
                candy[y][x], candy[y+1][x] = candy[y+1][x],candy[y][x]
                maxCandy = max(maxCandy, eatCandy(N,candy))
                candy[y][x], candy[y+1][x] = candy[y+1][x],candy[y][x]
    return maxCandy

N = int(input())
candy = [" ".join(input()).split() for _ in range(N)]
print(changeCandy(N))

# test = [['C', 'Y', 'P', 'Z', 'Y'], ['C', 'Y', 'Z', 'Z', 'P'], ['X', 'X', 'X', 'P', 'P'], ['Y', 'C', 'Y', 'Z', 'C'], ['C', 'P', 'P', 'Z', 'Z']]
# print(eatCandy(N,test))