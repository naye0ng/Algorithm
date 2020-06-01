"""
나무재테크
https://www.acmicpc.net/problem/16235
"""
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] # S2D2 양분
G = [[5]*N for _ in range(N)] # 양분

tree = [[[] for i in range(N)] for _ in range(N)]   # 나무
for _ in range(M) :
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
"""
[초기 배열 정렬] 
- 백준에서 이 부분 추가 안해도 에러가 발생 안함
- 같은 자리에 큰 나무 => 작은 나무 순으로 들어오는 입력이 없는 듯?
"""
for x in range(N) :
    for y in range(N) :
        if tree[x][y] :
            tree[x][y].sort()

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(K) :
    
    for x in range(N) :
        for y in range(N) :
            if tree[x][y] :
                # 봄
                next_tree, next_G = [], 0
                for t in tree[x][y] :
                    if G[x][y] >= t :
                        G[x][y]-= t
                        next_tree.append(t+1)
                    else :
                        next_G += t//2
                tree[x][y] = next_tree
                # 여름
                G[x][y] += next_G 

    # 가을
    for x in range(N) :
        for y in range(N) :
            # 가을
            for t in tree[x][y] :
                if t%5 == 0 :
                    for i in range(8) :
                        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N :
                            tree[x+dx[i]][y+dy[i]].insert(0,1)
            # 겨울
            G[x][y] += A[x][y]

S = 0
for x in range(N) :
    for y in range(N) :
        S += len(tree[x][y])              
                
print(S)