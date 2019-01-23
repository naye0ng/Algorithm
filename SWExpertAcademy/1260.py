"""
1260.화학물질
"""

def iswall(x,y) :
    if 0>x or x>=n : return True
    if 0>y or y>=n :return True
    if an[x][y] == 0 : return True

# 부분집합 처리
def subset(x,y) :
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dt = 0 #delta 제어
    # 행렬 크기 반환
    x1 = x-1
    y1 = y-1
    x2,y2 = 0,0
    while 1 :
        if an[x][y] == 0 :
            # 이미 치환되었다면?
            break
        an[x][y] = 0 
        x += dx[dt]
        y += dy[dt]
        if iswall(x,y) :
            x -= dx[dt]
            y -= dy[dt]
            if y2 == 0 :
                y2 =y
            elif x2 == 0 :
                x2 = x
            dt = (dt+1)%4
            x += dx[dt]
            y += dy[dt]

    return x2-x1, y2-y1

def minvalue(an) :
    k = len(an)

    if k == 1 :
        return an, 0
    min_s = 0
    min_kn = []
    for i in range(k-1) :
        bn, s1= minvalue(an[:i+1])
        cn, s2= minvalue(an[i+1:])

        s = bn[0][0]*bn[0][1]*cn[0][1]+s1+s2
        kn = [[bn[0][0],cn[0][1]]]

        if min_s == 0 :
            min_s = s
            min_kn =kn
        if min_s > s :
            min_s =s
            min_kn = kn
    return min_kn, min_s

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    an = [list(map(int,input().split())) for i in range(n)]

    # sub행렬의 크기
    subs = []
    heads = []
    tails = []

    for i in range(n) :
        for j in range(n) :

            if an[i][j] != 0 :
                # 함수호출
                head, tail = subset(i,j)
                heads.append(head)
                tails.append(tail)
                #subs.append(subset(i,j))
                
    # 최적의 곱하기 횟수subs를 구하자
    pt = 0
    for i in range(len(heads)) :
        if heads[i] not in tails :
            pt =i
            subs.append([heads[pt],tails[pt]]) 

    while len(subs) != len(heads):
        if tails[pt] in heads :
            pt = heads.index(tails[pt])
            subs.append([heads[pt],tails[pt]]) 

    last, result = minvalue(subs)

    print(f'#{test_case} {result}')
