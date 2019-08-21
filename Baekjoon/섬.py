"""
섬
https://www.acmicpc.net/problem/16000
"""
# 이어진 섬들에 대한 판별
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def makeIsland(N,M) :
    count = 0
    islandQ = []
    for x in range(1,N-1) :
        for y in range(1,M-1) :
            if island[x][y] == '#' :
                count += 1
                queue = []
                queue.append([x,y])
                islandQ.append([x,y])
                while queue :
                    q = queue.pop(0)
                    qx, qy = q[0], q[1]
                    island[qx][qy] = count
                    for i in range(4) :
                        if island[qx+dx[i]][qy+dy[i]] == '#' :
                            queue.append([qx+dx[i],qy+dy[i]])




                            
# def isboundary(N,M,x,y) :
#     if x == 0 or y == 0 or x == N-1 or y == M-1 :
#         return True
#     return False

# # count로 이어진 섬의 부모 찾기                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# def isSave(N,M,count,islandQ) :
#     for c in range(len(count)) :
#         queue = []
#         queue.append(islandQ[c])
#         isNotBreak = True
#         while queue and isNotBreak:
#             q = queue.pop(0)
#             x, y = q[0], q[1]
#             before = 0
#             for i in range(4) :
#                 # 같은 섬에 속한 것이 아닐 경우
#                 if  island[x][y] != island[x+dx[i]][y+dy[i]] :
                    # if isboundary(N,M,x,y) :
                    #     isNotBreak = True
                    #     break
                    # elif island[x+dx[i]][y+dy[i]] == '.' :
                    #     queue.append([x+dx[i],y+dy[i]])
                    # else :
                    #     if before == 0 :
                    #         before == island[x+dx[i]][y+dy[i]] 
                    #     else :
                    #         before != island[x+dx[i]][y+dy[i]] :

                


N, M = map(int,input().split())
island = [ " ".join(input()).split() for _ in range(N)]
makeIsland(N,M)
print(island)