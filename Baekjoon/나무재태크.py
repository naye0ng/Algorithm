"""
나무재테크
https://www.acmicpc.net/problem/16235
"""
def is_not_wall(x,y) :
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= N :
        return False
    return True


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] 

trees = [[[] for n in range(N)] for _ in range(N)]
food = [[5]*N for _ in range(N)]

for _ in range(M) :
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(K) : 
    # 가을
    fall = []
    result = 0
    for x in range(N) :
        for y in range(N) :
            if trees[x][y] :
                # 봄
                # f = 0
                trees[x][y].sort()
                """
                [시간초과]
                [1] pop과 append의 잦은 사용이 문제!
                [2] 작 -> 큰 순서대로 이므로 else 이후로 [idx:]는 break 처리
                """
                idx = 0
                while idx < len(trees[x][y]) :
                    if trees[x][y][idx] <= food[x][y] :
                        result += 1
                        food[x][y] -= trees[x][y][idx]
                        trees[x][y][idx] += 1
                        if (trees[x][y][idx])%5 == 0 :
                            fall.append([x,y])
                        idx += 1
                    else : 
                        die = trees[x][y][idx:]
                        for tree in die :
                            # 여름
                            food[x][y] += tree//2
                        trees[x][y] = trees[x][y][:idx]
                        break
                """
                # 시간초과 코드
                for i in range(len(trees[x][y])) :
                    tree = trees[x][y].pop(0)
                    if tree <= food[x][y] :
                        result += 1
                        food[x][y] -= tree
                        trees[x][y].append(tree+1)
                        if (tree+1)%5 == 0 :
                            fall.append([x,y])
                    else :
                        f += tree//2
                여름
                food[x][y] += f
                """
            # 겨울
            food[x][y] += A[x][y]

    for i in range(len(fall)) :
        x, y = fall[i]
        for k in range(8) :
            if is_not_wall(x+dx[k],y+dy[k]) :
                trees[x+dx[k]][y+dy[k]].append(1)
                result += 1
print(result)


"""
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

답 : 15
---------------
10 10 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1
2 2 1
3 3 1
4 4 1
5 5 1
6 6 1
7 7 1
8 8 1
9 9 1
10 10 1

답 : 5150
"""