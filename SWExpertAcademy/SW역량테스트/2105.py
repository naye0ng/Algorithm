"""
디저트 카페
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
"""

def isNotWall(N,x,y) :
    if x >= 0 and x < N :
        if y >= 0 and y < N :
            return True
    return False 

dx = [-1,1,1,-1]
dy = [1,1,-1,-1]

def visitCafe(N) :
    for x in range(1,N-1) :
        for y in range(N-2) :
            Gx, Gy = x, y
            dessert = [False]*101
            dessert[cafe[x][y]] = True
            i = 0
            arrI = [0,0,0,0]
            path = [[x,y]]
            while i < 4 :
                if i <= 1 :
                    if isNotWall(N,startY,x+dx[i],y+dy[i]) and dessert[cafe[x+dx[i]][y+dy[i]]] == False :
                        x += dx[i]
                        y += dy[i]
                        dessert[cafe[x][y]]= True
                        path.append([x,y])
                        arrI[i] += 1
                    else :
                        i += 1
                    continue
                notBreak =True
                while notBreak :
                    pass
                     





    #         i, startX, startY = 0, x, y 
    #         dessert = [False]*101
    #         dessert[cafe[x][y]] = True
    #         path = [[x,y,-1]]
    #         good = False
    #         while i < 4:
    #             if x+dx[i] == startX and y+dy[i] == startY :
    #                 good = True
    #                 break
    #             # 다음 디저트가 먹을 수 있고 벽이 아니라면
    #             if isNotWall(N,startY,x+dx[i],y+dy[i]) and i <= 3 :
    #                 if dessert[cafe[x+dx[i]][y+dy[i]]] == False :
    #                     x += dx[i]
    #                     y += dy[i]
    #                     dessert[cafe[x][y]]= True
    #                     path.append([x,y,i])
    #                 else :
    #                     # 벽은 아닌데 디저트를 먹을 수 없는 --> 중복된 번호 존재
    #                     l = len(path)-1
    #                     breakPT = True
    #                     while l > 0 :
    #                         px, py, pi = path[l][0],path[l][1],path[l][2]    
    #                         if pi == path[l-1][2] and pi <= 1 :
    #                             i = (pi + 1)
    #                             breakPT = False
    #                             break
    #                         else :
    #                             p = path.pop()
    #                             dessert[cafe[p[0]][p[1]]] = False
    #                         l -= 1
    #                     if breakPT :
    #                         break
    #             else : 
    #                 i += 1
    #                 path[-1][2] = i
    #         if good :
    #             print(path)
        
T = int(input())
for t in range(1,T+1) :
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visitCafe(N) 
    print('#{} {}'.format(t,t))