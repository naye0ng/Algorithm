"""
미생물 격리
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""

# 상 좌 하 우
dx = [-1,0,1,0]
dy = [0,-1,0,1]

T = int(input())
for test_case in range(1, 1+T) :
    N, M, K = map(int,input().split())

    # 군집 개수만들기
    group = []
    for _ in range(K) :
        x, y, cnt, d = map(int,input().split())
        if d == 2 :
            d = 3
        elif d == 3 :
            d = 2
        group.append([x,y,cnt,d-1])
    t = 0
    while t < M :
        # [1] 1회 이동
        for i in range(K) :
            # 군집이 존재한다면
            if group[i][2] :
                x, y, cnt, d = group[i]
                # 약품과 만난다면
                nextD = d
                if x+dx[d] == 0 or x+dx[d] == N-1 or y+dy[d] == 0 or y+dy[d] == N-1 :
                    nextD = (d+2)%4
                    cnt = cnt//2
                group[i] = [x+dx[d],y+dy[d],cnt,nextD]

        # [2] 겹치는 것 처리
        for i in range(K-1) :
            if group[i][2] :
                x, y, cnt, d = group[i]
                maxCnt = cnt
                for j in range(i+1,K) :
                    if group[j][2] and x == group[j][0] and y == group[j][1] :
                        # 최대값 구하기
                        if group[j][2] > maxCnt :
                            maxCnt = group[j][2]
                            d = group[j][3]
                        cnt += group[j][2]
                        group[j][2] = 0
                group[i][2], group[i][3] = cnt, d
        t += 1

    result = 0
    for g in group :
        result += g[2]
    print('#{} {}'.format(test_case, result))

"""
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1

1
10 17 46
7 5 724 2
7 7 464 3
2 2 827 2
2 4 942 4
4 5 604 4
7 2 382 1
6 5 895 3
8 7 538 4
6 1 299 4
4 7 811 4
3 6 664 2
6 8 868 2
7 6 859 2
4 6 778 2
5 4 842 3
1 3 942 1
1 1 805 3
3 2 350 3
2 5 623 2
5 3 840 1
7 1 308 4
1 8 323 3
2 3 82 3
2 6 115 2
8 3 930 1
6 2 72 1
2 1 290 3
4 8 574 4
8 5 150 3
8 2 287 2
2 8 909 2
2 7 588 2
7 3 30 3
5 8 655 3
3 8 537 1
4 2 350 3
5 6 199 1
5 5 734 2
3 3 788 1
8 4 893 1
1 4 421 4
6 3 616 2
1 2 556 4
7 8 8 1
5 2 702 2
4 4 503 3




"""