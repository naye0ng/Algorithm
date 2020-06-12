champions_league = {}
N = int(input())
for _ in range(N*(N-1)) :
    t1, r1, t2, r2 = input().split()
    r1, r2 = int(r1), int(r2)
    if t1 not in champions_league :
        champions_league[t1] = [t1.upper(),0,0,0,0] # 이름, 승, 패, 승득, 패득, 득실
        # champions_league[t1] = [t1.upper(),0,0,0,0,0] # 이름, 승, 패, 승득, 패득, 득실

    if t2 not in champions_league :
        champions_league[t2] = [t2.upper(),0,0,0,0]
        # champions_league[t2] = [t2.upper(),0,0,0,0]


    if r1 > r2 :
        champions_league[t1][1] += 1
        champions_league[t2][2] += 1
    else :
        champions_league[t1][2] += 1
        champions_league[t2][1] += 1
    champions_league[t1][3] += r1
    champions_league[t1][4] += r2
    champions_league[t2][3] += r2
    champions_league[t2][4] += r1

    # TODO :여기서 패득 계산 매번 해주면?
    # champions_league[t1][5] = champions_league[t1][3] - champions_league[t1][4]
    # champions_league[t2][5] = champions_league[t2][3] - champions_league[t2][4]


# for arr in sorted(list(champions_league.values()),key = lambda x : (-x[1], -x[5], x[0])) :
#     print(arr[0], arr[1], arr[5])

rank = []
# 세트 득실 계산
for name, win, lose, c_win, c_lose in champions_league.values() :
    rank.append([win,c_win-c_lose, name])

for win, w_l, name in sorted(rank, key = lambda x : (-x[0], -x[1], x[2])) :
    print(name, win, w_l)

"""
4
drx 2 t1 1
drx 1 gen 2
t1 1 gen 2
t1 2 drx 1
kt 1 drx 2
t1 0 kt 2
drx 2 kt 1
gen 1 t1 2
gen 2 kt 0
gen 1 drx 2
kt 0 t1 2
kt 2 gen 0

drx 4 2
gen 3 0
t1 3 0
kt 2 -2
"""
