"""
사다리조작
https://www.acmicpc.net/problem/15684
"""
def checkPath(N, H) :
    for b in range(N) :
        start, a, RL = b, 0, False
        while a < H :
            # 오왼으로 이동해 온것이라면, 이동한 적이 있다면
            if RL :
                RL = False
                a += 1
            else :
                if arr[a][b] == 0 :
                    a += 1
                elif arr[a][b] == 1 :
                    b += 1
                    RL = True
                elif arr[a][b] == 2 :
                    b -= 1 
                    RL = True
        if start != b :
            return False
    return True

def addpath(N, H) :
    # 아무것도 안뽑음
    if checkPath(N, H) :
        return 0
    #  1개 추가
    i = 0
    while i < len(paths) :
        arr[paths[i][0]][paths[i][1]], arr[paths[i][0]][paths[i][1]+1] =  1, 2
        if checkPath(N, H) :
            return 1
        arr[paths[i][0]][paths[i][1]] = arr[paths[i][0]][paths[i][1]+1] = 0
        i += 1
    
    #  make combination
    L = len(paths)
    path2 = []
    path3 = []
    for i in range(L) :
        for j in range(i+1, L) :
            path2.append([paths[i],paths[j]])
            for k in range(j+1, L) :
                path3.append([paths[i], paths[j], paths[k]])
    for path in path2 :
        if arr[path[0][0]][path[0][1]] == 0 and  arr[path[0][0]][path[0][1]+1] == 0 and arr[path[1][0]][path[1][1]]==0 and arr[path[1][0]][path[1][1]+1] ==0 : 
            arr[path[0][0]][path[0][1]], arr[path[0][0]][path[0][1]+1] =  1, 2
            arr[path[1][0]][path[1][1]], arr[path[1][0]][path[1][1]+1] =  1, 2
            if checkPath(N, H) :
                return 2
            arr[path[0][0]][path[0][1]] = arr[path[0][0]][path[0][1]+1] =  0
            arr[path[1][0]][path[1][1]] = arr[path[1][0]][path[1][1]+1] =  0
    for path in path3 :
        if arr[path[0][0]][path[0][1]] == 0 and  arr[path[0][0]][path[0][1]+1] == 0 and arr[path[1][0]][path[1][1]]==0 and arr[path[1][0]][path[1][1]+1] ==0 and arr[path[2][0]][path[2][1]] == 0 and arr[path[2][0]][path[2][1]+1] == 0 : 
            arr[path[0][0]][path[0][1]], arr[path[0][0]][path[0][1]+1] =  1, 2
            arr[path[1][0]][path[1][1]], arr[path[1][0]][path[1][1]+1] =  1, 2
            arr[path[2][0]][path[2][1]], arr[path[2][0]][path[2][1]+1] =  1, 2
            if checkPath(N, H) :
                return 3
            arr[path[0][0]][path[0][1]] = arr[path[0][0]][path[0][1]+1] =  0
            arr[path[1][0]][path[1][1]] = arr[path[1][0]][path[1][1]+1] =  0
            arr[path[2][0]][path[2][1]] = arr[path[2][0]][path[2][1]+1] =  0
    return -1


N, M, H = map(int, input().split())
arr = [ [0]*N for _ in range(H)]

if H != 0 :
    for _ in range(M) :
        a, b = map(int, input().split())
        arr[a-1][b-1], arr[a-1][b] = 1, 2
    # paths : 이동가능한 경로 : [x,y] -> [x,y+1]
    paths = []
    for x in range(H) :
        for y in range(N-1) :
            if arr[x][y] == 0 and arr[x][y+1] == 0 :
                paths.append([x,y])

print(addpath(N, H))