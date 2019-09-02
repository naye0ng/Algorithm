def isWall(x,y) :
    if x < -1000 or x > 1000 :
        return True
    if y < -1000 or y > 1000 :
        return True
    return False

def checkAtoms(N, result) :
    # 만약 같은 것이 있거나 본인이 index를 벗어날때
    for i in range(N) :
        x, y = atoms[i][0], atoms[i][1]
        if outAtoms[i] == 0 :
            if isWall(x,y) :
                outAtoms[i] = 1 
            else :
                check = False
                for j in range(i+1,N) :
                    if outAtoms[j] == 0 and (x == atoms[j][0] and y == atoms[j][1]) :
                        result += atoms[j][3]
                        outAtoms[j] = 1
                        check = True
                if check :
                    outAtoms[i] = 1
                    result += atoms[i][3]  
    return result

# 상하좌우
dx = [0,0,-0.5,0.5]
dy = [0.5,-0.5,0,0]
def moveAtoms(N, result) :
    while True :
        for i in range(N) :
            if outAtoms[i] == 0 :
                atoms[i][0] += dx[atoms[i][2]]
                atoms[i][1] += dy[atoms[i][2]]
        result = checkAtoms(N, result)
        if sum(outAtoms) == N :
            return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    outAtoms = [0]*N
    print('#{} {}'.format(test_case, moveAtoms(N, 0)))

"""
1
10
-998 0 2 8
-5 0 3 4
5 0 2 1
998 0 3 7
0 -5 0 5
0 6 1 9
5 3 3 8
6 3 3 5
7 3 3 1
10 3 2 5

답 : 16
"""