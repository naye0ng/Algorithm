"""
이차원배열과연산
https://www.acmicpc.net/problem/17140
"""
def isNotWall(x,y) :
    global row, col
    if x < 0 or x >= row :
        return False
    if y < 0 or y >= col :
        return False
    return True

# 행단위 연산
def sortedByRow(col) :
    global A
    new_A = [ [] for _ in range(len(A))]
    for x in range(len(A)) :
        visited = [0 for _ in range(101)]
        for y in range(len(A[x])) :
            visited[A[x][y]] += 1
        # 숫자 i가 visited[i]번 나온다.
        order = {}
        for i in range(1, 101) :
            if not visited[i] : continue

            if visited[i] not in order :
                order[visited[i]] = set()
            order[visited[i]].add(i)
        
        # key 순서대로 정렬
        cnts = sorted(order)
        for cnt in cnts :
            for number in sorted(order[cnt]) :
                new_A[x].extend([number,cnt])
        """
        [실패이유]
        col은 0이 되서 들어와야 이전에 수행된 안겹침!!!
        """
        # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
        col = min(max(col, len(new_A[x])), 100)
    # 최대 col 맞춰서 배열 생성
    for x in range(len(A)) :
        if len(new_A[x]) > col :
            new_A[x] = new_A[x][:100]
        else :
            l = col-len(new_A[x])
            new_A[x] += [0]*l
    # global A
    A = new_A
    return col

def sortedByCol(row) :
    global A
    new_A = [[] for _ in range(len(A[0]))]
    for y in range(len(A[0])) :
        visited = [0 for _ in range(101)]
        for x in range(len(A)) :
            visited[A[x][y]] += 1
        order = {}
        for i in range(1, 101) :
            if not visited[i] : continue

            if visited[i] not in order :
                order[visited[i]] = set()
            order[visited[i]].add(i)
        
        cnts = sorted(order)
        for cnt in cnts :
            """
            [실패이유] python set이 항상 정렬될 것이라 생각하지 말 것!
            sorted(set())이 가능한 이유를 생각해 봐라!
            """
            for number in sorted(order[cnt]) :
                new_A[y].extend([number,cnt])
        row = min(max(row, len(new_A[y])), 100)
    # 최대 row 맞처서 생성
    for y in range(len(A[0])) :
        # row 보다 큰 경우는 자름
        if len(new_A[y]) > row :
            new_A[y] = new_A[y][:100]
        else :
            l = row-len(new_A[y])
            new_A[y] += [0]*l
    # A 다시 구성
    A2 = [ [0]*len(A[0]) for _ in range(row)]
    for x in range(row) :
        for y in range(len(A[0])) :
            A2[x][y] = new_A[y][x]
    A = A2
    return row
    

R, C, K = map(int, input().split())
row, col = 3, 3 # 행수, 열수
A = [list(map(int, input().split())) for _ in range(row)]

T = -1
for t in range(101) :
    """ 
    [런타임에러] 주언진 배열의 크기가 변하므로 애초에 검색될 범위를 벗어날 수 있다.
    4 4 4
    3 3 3 
    3 3 3
    3 3 3
    """
    if isNotWall(R-1,C-1) and A[R-1][C-1] == K :
        T = t
        break

    if row >= col : col = sortedByRow(0)
    else : row = sortedByCol(0)

print(T)

"""
100 100 1
9 2 3 2 4 8 3 4 9 4 10 4 4 4 4 4
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
5 13 5 11 6 3 5 1 3 1 4 5 1 1 1 5
1 1 1 1 1 1 1 2 1 2 1 1 2 2 2 1
2 1 6 1 7 5 6 3 5 3 2 2 3 3 3 2
2 3 1 3 1 1 1 2 1 2 2 2 2 2 2 2
3 3 4 3 2 4 7 2 4 2 1 1 2 2 2 1
2 3 2 3 2 2 1 3 2 3 3 3 3 3 3 3
4 0 1 0 3 1 2 0 1 0 3 3 0 0 0 3
2 0 3 0 2 3 2 0 3 0 3 3 0 0 0 3
1 0 2 0 5 2 4 0 2 0 0 0 0 0 0 0
4 0 4 0 2 4 3 0 4 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 5 0 5 0 0 0 0 0 0 0 0 0
"""
