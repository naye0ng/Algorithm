"""
1976.시각 덧셈
"""
T = int(input())
for test_case in range(1,1+T):
    t1, m1, t2, m2 = map(int, input().split())

    t = (m1+m2)//60
    m = (m1+m2)%60

    t = (t1+t2+t)%12
    if t == 0 :
        t = 12

    print(f'#{test_case} {t} {m}')