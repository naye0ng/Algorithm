"""
5648 - 원자소멸 시뮬레이션
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo&categoryId=AWXRFInKex8DFAUo&categoryType=CODE
"""

# 상(0), 하(1), 좌(2), 우(3)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
board = [[False]*4000 for _ in range(4000)]
def oneLoop(N, atoms) :
    score = 0
    while atoms :
        # 이동
        crush = set()
        next_atoms = []
        for i in range(len(atoms)) :
            x,y,d,k = atoms[i]
            # 이전 값 지우기
            board[x][y] = False
            x += dx[d]
            y += dy[d]
            if (x >= -2000 and x < 2000) and (y >= -2000 and y < 2000) :
                # 겹치는 것이 있다면?
                if board[x][y] :
                    score += k
                    crush.add((x,y))
                else :
                    board[x][y] = True
                    next_atoms.append([x,y,d,k])
        # 다음 값들 중 겹치는 값 지우기
        if len(crush) >= 1 :
            for i in range(len(next_atoms)-1,-1,-1) :
                x, y = next_atoms[i][0], next_atoms[i][1]
                if (x,y) in crush :
                    score += next_atoms[i][3]
                    board[x][y] = False
                    next_atoms.pop(i)
                if len(crush) == 0 :
                    break
        atoms = next_atoms
    return score


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    for atom in atoms :
        atom[0] = atom[0]*2
        atom[1] = atom[1]*2
        board[atom[0]][atom[1]] = 1
    print("#{} {}".format(test_case, oneLoop(N, atoms)))
