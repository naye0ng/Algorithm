"""
인구이동
https://www.acmicpc.net/problem/16234
"""
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def isNotWall(N,x,y) :
    if x >= 0 and x <= N-1 :
        if y >= 0 and y <= N-1 :
            return True
    return False

def movePeople(N, L, R, depth) :
    visited = [ [False]*N for _ in range(N)]
    isEnd = True
    for x in range(N) :
        for  y in range(N) :
            if visited[x][y] == False : 
                queue = []
                total = 0
                makeSum = []
                queue.append([x,y])
                while queue :
                    q = queue.pop(0)
                    qx, qy = q[0], q[1]
                    if visited[qx][qy] == False :
                        visited[qx][qy] = True
                        total += people[qx][qy]
                        makeSum.append(q)
                        for i in range(4) :
                            if isNotWall(N, qx+dx[i], qy+dy[i]) and visited[qx+dx[i]][qy+dy[i]] == False:
                                t = abs(people[qx][qy] - people[qx+dx[i]][qy+dy[i]]) 
                                if t >= L and t <= R :
                                    queue.append([qx+dx[i], qy+dy[i]])
                # 계산하기
                l = len(makeSum)
                if l > 1 :
                    isEnd = False
                    aver = total//l
                    for i in range(l) :
                        people[makeSum[i][0]][makeSum[i][1]] = aver
                total = 0
                makeSum = []
    if isEnd :
        return depth
    return movePeople(N, L, R, depth+1)




N, L, R = map(int, input().split())
people = [ list(map(int, input().split())) for _ in range(N) ]
print(movePeople(N,L,R,0))
