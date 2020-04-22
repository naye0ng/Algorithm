"""
원자소멸시뮬레이션
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo
"""
"""
[주의] 
(1) 문제가 x, y 좌표계를 따르는지, 행렬 좌표를 따르는지 꼭 확인하자!
(2) 증가 방향이 보편적인 값이 아닐 수 있다!!!
 - 상: y 가 증가하는 방향
 - 하: y 가 감소하는 방향
 - 좌: x 가 감소하는 방향
 - 우: x 가 증가하는 방향
"""
dy = [1,-1,0,0]
dx = [0,0,-1,1]
"""
[런타임에러]
어차피 visited는 계속 비어있는 값이 유지되므로 전역으로 분리
>> visited 배열은 2차원처럼 보이지만, 0 <= ?(+) <= 2000까지, 2001(=-2000) <= ?(-) <= 4002(-1)로 나눠짐
"""
visited = [[False]*4001 for _ in range(4001)]

T = int(input())
for test_case in range(1, 1+T) :
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    for i in range(len(atoms)) :
        atoms[i][0], atoms[i][1] = atoms[i][0]*2, atoms[i][1]*2
        visited[atoms[i][0]][atoms[i][1]] = True

    E = 0
    while len(atoms) > 1 :
        """
        [시간초과]
        두 원자가 만나서 소멸될 수 있는 위치는 중간 값인 .5 혹은 1뿐이다.
        즉, .5에 위치해있는 원자와 1에 위치한 원자가 만나서 소멸되는 경우는 존재하지 않는다.
        이말은 atoms 배열안에 있는 원자를 한번씩 모두 이동할 필요 없이, 하나씩 수행해도 된다는 말이다.
        """
        crush = set()
        next_atoms = []
        for i in range(len(atoms)) :
            x, y, d, e = atoms[i]
            visited[x][y] = False
            x += dx[d]
            y += dy[d]

            """
            [시간초과2]
            next_atoms의 원소가 많으면 시간초과가 발생할 수 있다. => visited 배열을 사용하자!
            """
            if (-2000 <= x <= 2000) and (-2000 <= y <= 2000) :
                if not visited[x][y] :
                    visited[x][y] = True
                    next_atoms.append([x,y,d,e])
                else :
                    E += e
                    crush.add((x,y))
        # 충돌 값 지우기
        if len(crush) >= 1 :
            for i in range(len(next_atoms)-1,-1,-1) :
                if (next_atoms[i][0], next_atoms[i][1]) in crush :
                    visited[next_atoms[i][0]][next_atoms[i][1]] = False
                    E += next_atoms.pop(i)[3]
        atoms = next_atoms

    print('#{} {}'.format(test_case, E))

"""
1
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9
"""