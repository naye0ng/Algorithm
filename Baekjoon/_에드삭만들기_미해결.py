"""
에드삭만들기
https://www.acmicpc.net/problem/2677
"""
from decimal import Decimal
teletype = "PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV"

P = int(input())

for _ in range(P) :
    D = Decimal(input())
    if D < Decimal(-1.0) or D >= Decimal(1.0) :
        print("INVALID VALUE")
        continue

    bit17 = '0'
    bit16 = [0]*16
    if D == -1.0 :
        # -1.0일때 소수점 아래 변환 안함
        bit17 = '1'
        D = 0

    elif D < 0 :
        D = D*(-1)
        if D < -0.0000152587890624 :
            bit17 = '2'
        else : 
            bit17 = '1'
    # 2진수 변환
    for i in range(16) :
        if D == 0 :
            break
        D = D * 2
        if D >= 1 :
            D-= 1
            bit16[i] = 1

    # 범위에서 벗어난 수는 올림처리
    if bit17 == '2' :
        bit17 = '1'
        # 1의 보수
        for i in range(16) :
            bit16[i] = (bit16[i]+1)%2 
        # +1 더하기
        up = 1
        for i in (15,-1,-1) :
            if up == 0 :
                break
            up == bit16[i]
            bit16[i] = (bit16[i] + 1)%2
    bit16 = list(map(str, bit16))
    print(teletype[int(bit17+"".join(bit16[:4]),2)], int("".join(bit16[4:-1]),2), 'F' if bit16[-1] == '0' else 'D')
    
"""
(음수변환 : 1의 보수 => +1)

-0.0000152587890624
P 0 F
"""