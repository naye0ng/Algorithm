"""
배열돌리기4
https://www.acmicpc.net/problem/17406
"""
import copy

def rotate(k, order) :
    if k == K :
        # order 순서대로 회전
        A2 = copy.deepcopy(A)
        for i in order :
            r, c, s = queue[i]
            bx1, by1, bx2, by2 = r-s-1, c-s-1, r+s, c+s
            # print(bx1, by1, bx2, by2, bx2-bx1,by2-by1, min(bx2-bx1,by2-by1)//2)
            for t in range(min(bx2-bx1,by2-by1)//2) :
                temp = A2[bx1+t][by1+t]
                # →
                for y in range(by1+t+1, by2-t) :
                    A2[bx1+t][y], temp = temp, A2[bx1+t][y]
                # ↓
                for x in range(bx1+t+1, bx2-t) :
                    A2[x][by2-t-1], temp = temp, A2[x][by2-t-1]
                # ←
                for y in range(by2-t-2, by1+t-1, -1) :
                    A2[bx2-t-1][y], temp = temp, A2[bx2-t-1][y]
                # ↑
                for x in range(bx2-t-2,bx1+t-1, -1) :
                    A2[x][by1+t], temp = temp, A2[x][by1+t]
        global min_S
        min_S = min(min_S, min([sum(A2[i]) for i in range(N)]))
    else :
        for i in range(K) :
            if not visited[i] :
                visited[i] = True
                rotate(k+1, order+[i])
                visited[i] = False

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
queue = []
for _ in range(K) :
    queue.append(list(map(int, input().split())))

min_S = 5000    # 50*1000
visited = [False]*K
rotate(0, [])
print(min_S)