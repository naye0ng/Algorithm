"""
5656 - 벽돌깨기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE
"""
import copy

def isNotWall(x,y) :
    global H, W 
    if x >= 0 and x < H :
        if y >= 0 and y < W :
            return True
    return False

# 공에 맞음  
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def crushBlock(W,H,N,B,blocks) :
    b = 0
    while b < N :
        visited = [[False]*W for _ in range(H)]
        for x in range(H) :
            if blocks[x][B[b]] != 0 :
                visited[x][B[b]] = True
                queue = [[x,B[b]]]
                while queue :
                    q = queue.pop(0)
                    for i in range(4) :
                        for k in range(1,blocks[q[0]][q[1]]) :
                            if isNotWall(q[0]+dx[i]*k,q[1]+dy[i]*k) :
                                if blocks[q[0]+dx[i]*k][q[1]+dy[i]*k] != 0 and visited[q[0]+dx[i]*k][q[1]+dy[i]*k] == False :
                                    visited[q[0]+dx[i]*k][q[1]+dy[i]*k] = True
                                    queue.append([q[0]+dx[i]*k,q[1]+dy[i]*k])
                            else :
                                break
                break
        # 정렬
        for y in range(W) :
            stack = []
            for x in range(H-1,-1,-1) :
                if visited[x][y] == False :
                    stack.append(blocks[x][y])
                blocks[x][y] = 0
            k = 0
            while k < len(stack) :
                blocks[-1*(k+1)][y] = stack[k]
                k += 1
        b += 1
    # 남은 수 계산
    num = 0
    for x in range(H) :
        for y in range(W) :
            if blocks[x][y] != 0 :
                num += 1
    return num


def chooseBlock(W,H,N,depth,block,blocks) :
    global result
    if depth == N :
        result = min(result,crushBlock(W,H,N,block,copy.deepcopy(blocks)))
    else :
        for i in range(W) :
            chooseBlock(W,H,N,depth+1,block+[i],blocks)

T = int(input())
for test_case in range(1, T+1) :
    N, W, H = map(int, input().split())
    blocks = [ list(map(int, input().split())) for _ in range(H)]
    result = W*H
    chooseBlock(W,H,N,0,[], blocks)
    print("#{} {}".format(test_case, result))
