"""
야구
https://www.acmicpc.net/problem/17281
"""
max_score = 0
# 득점 계산
def get_score(player) :
    """
    [시간초과] 
    배열 쓰는거 자체가 사치
    """
    b1, b2, b3 = 0, 0, 0 # 1루 2루 3루
    score = 0
    idx, inning_idx, out = 0, 0, 0
    while inning_idx < N :
        play = inning[inning_idx][player[idx]]
        if play == 0 :
            # 아웃
            out += 1
            if out == 3 :
                # 다음 이닝 진행 >> 모두 초기화!
                inning_idx += 1
                out, b1, b2, b3 = 0, 0, 0, 0
        elif play == 1 :
            # 안타 - 모두 한 루씩 이동
            score += b3
            b3, b2, b1 = b2, b1, 1
        elif play == 2 :
            # 2루타 - 모두 두 루씩 이동
            score += b3 + b2
            b3, b2, b1 = b1, 1, 0
        elif play == 3 :
            # 3루타 - 모두 세 루씩 이동 
            score += b3 + b2 + b1
            b3, b2, b1 = 1, 0, 0
        elif play == 4 :
            # 홈런
            score += b3 + b2 + b1 +1
            b1, b2, b3 = 0, 0, 0
        idx = (idx+1)%9

    global max_score 
    max_score = max(max_score, score)

# 타순 정하기
def get_player(n, player) :
    if n == 9 : 
        get_score(player)
    elif n == 4 :
        get_player(n+1, player)
    else :
        for i in range(9) :
            if not visited[i] :
                visited[i] = True
                player[n] = i
                get_player(n+1, player)
                player[n] = 0
                visited[i] = False

N = int(input())
inning = [[] for _ in range(N)]

for i in range(N) :
    inning[i] = list(map(int, input().split()))

visited = [False]*9
visited[0] = True
get_player(0, [0]*9) 

print(max_score)