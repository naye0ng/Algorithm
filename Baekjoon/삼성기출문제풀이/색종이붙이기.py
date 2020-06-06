"""
색종이붙이기
https://www.acmicpc.net/problem/17136
"""
def is_not_wall(x, y) :
    if x < 0 or x >= 10 :
        return False
    if y < 0 or y >= 10 :
        return False
    return True

def cover_paper(cnt, P) :
    global paper_cnt
    if cnt < paper_cnt :
        if P == 0 :
            paper_cnt = cnt
        else :
            is_break = False
            for x in range(10) :
                for y in range(10) :
                    if board[x][y] :
                        is_break = True
                        for size in range(5,0,-1) :
                            if paper[size] == 0 :
                                continue
                            n = 0
                            for a in range(x, x+size) :
                                for b in range(y, y+size) :
                                    if is_not_wall(a,b) and board[a][b] :
                                        n +=1
                            if n == size*size :
                                # size 색종이로 덮어진다.
                                for a in range(x, x + size):
                                    for b in range(y, y + size):
                                        board[a][b] = 0

                                paper[size] -= 1
                                cover_paper(cnt+1, P-n)
                                paper[size] += 1

                                for a in range(x, x + size):
                                    for b in range(y, y + size):
                                        board[a][b] = 1
                        break
                if is_break :
                    break

board = [list(map(int, input().split())) for _ in range(10)]

paper = [0,5,5,5,5,5]
paper_cnt = 26
cover_paper(0, sum(sum(board[i]) for i in range(10)))
if paper_cnt == 26 :
    print(-1)
else :
    print(paper_cnt)