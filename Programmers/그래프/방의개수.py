dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def solution(arrows):
    i, x, y = 0, 0, 0
    E = 0
    G = [[]]
    V = [[x, y]]
    for d in arrows :
        x2, y2 = x+dx[d], y+dy[d]
        if [x2, y2] not in V :
            V.append([x2, y2])
            G.append([])

        i2 = V.index([x2, y2])
        G[i].append(i2)
        G[i2].append(i)
        E += 1
        i, x, y = i2, x2, y2
   
    return 1+E-len(V)




print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))


