"""
원자소멸시뮬레이션
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo
"""
"""
- 상: y 가 증가하는 방향
- 하: y 가 감소하는 방향
- 좌: x 가 감소하는 방향
- 우: x 가 증가하는 방향
"""
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[-1]*4001 for _ in range(4001)]

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    atoms = [0]*N

    for i in range(N) :
        x, y, d, e = map(int, input().split())
        atoms[i] = [x*2, y*2, d, e]
        visited[x*2][y*2] = i
        
    # 0.5초 단위로 이동
    E = 0
    while len(atoms) >= 1 :
        next_atoms = []
        crush = set()
        for i in range(len(atoms)) :
            x, y, d, e = atoms[i]
            visited[x][y] = -1
            x += dx[d]
            y += dy[d]
            if -2000 <= x <= 2000 and -2000 <= y <= 2000 :
                if visited[x][y] == -1:
                    visited[x][y] = len(next_atoms)
                    next_atoms.append([x,y,d,e])
                else :
                    crush.add(visited[x][y])
                    E += e
        del_cnt = 0
        for c in crush :
            # visited 해제
            visited[next_atoms[c-del_cnt][0]][next_atoms[c-del_cnt][1]] = -1
            E += next_atoms.pop(c-del_cnt)[3]
            del_cnt += 1

        atoms = next_atoms

    print('#{} {}'.format(test_case, E))