"""
색종이붙이기
https://www.acmicpc.net/problem/17136
"""
def cover(n, c) :
    global N
    if n < N :
        if c == C :
            N = n
        else :
            # 왼쪽 최상단 빈칸 찾아서 5 => 1까지 모두 돌기
            for x in range(10) :
                for y in range(10) :
                    if not visited[x][y] :
                        # 덮을 수 있는 크기 조사
                        for k in range(5,0,-1) :
                            if paper[k] and x+k <= 10 and y+k <= 10 :
                                S = 0
                                for a in range(x, x+k) :
                                    for b in range(y, y+k) :
                                        if not visited[a][b] :
                                            S += 1
                                if S == k*k :
                                    for a in range(x, x + k):
                                        for b in range(y, y + k):
                                            visited[a][b] = True
                                    paper[k] -= 1
                                    cover(n+1, c+k*k)
                                    paper[k] += 1
                                    for a in range(x, x + k):
                                        for b in range(y, y + k):
                                            visited[a][b] = False
                        """
                        [시간초과 해결] 
                        왼쪽 최상단 빈칸을 찾았으면 이중 for문 종료시킨다!
                        - 이중 for문을 나가는 것이므로 break 두개 써야한다. 그냥 return 사용하자
                        [버릇을 만들자!]
                        for문을 종료해야겠거나, 갱신할 값이 있다면 미리 써두고 내부 구현을 진행하자!
                        """
                        return

board = [list(map(int, input().split())) for _ in range(10)]
visited = [[True]*10 for _ in range(10)]
paper = [0,5,5,5,5,5]

N, C = 26, 0
for x in range(10) :
    for y in range(10) :
        if board[x][y] :
            visited[x][y] = False
            C += 1

cover(0, 0)
if N == 26 :
    N = -1
print(N)

"""
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 0 0 0 0 1

5
"""
