"""
5644 - 무선충전
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE
"""
# 겹치는 것 검색
def getBC(N,x,y) :
    can_use = []
    for i in range(N) :
        bcX, bcY, c, p = battery_charger[i]
        if  abs(bcX-x)+abs(bcY-y) <= c :
            can_use.append([p,i])
    return sorted(can_use, reverse=True)

# 상(1), 우(2), 하(3), 좌(4)
dy = [0,-1,0,1,0]
dx = [0,0,1,0,-1]
T = int(input())
for test_case in range(1, T + 1):
    M, N = map(int, input().split()) # 총 이동시간, 총 bc수
    dA = [0] + list(map(int,input().split())) # A의 이동경로
    dB = [0] + list(map(int,input().split()))  # B의 이동경로
    battery_charger = [ list(map(int,input().split())) for _ in range(N)]

    ay, ax, by, bx = 1, 1, 10, 10
    m, result = 0, 0
    while m <= M :
        ay += dy[dA[m]]
        ax += dx[dA[m]]
        by += dy[dB[m]]
        bx += dx[dB[m]]

        aBC = getBC(N,ax,ay)
        bBC = getBC(N,bx,by)
        al = len(aBC)
        bl = len(bBC)

        if al == 0 and bl == 1 :
            result += bBC[0][0]
        elif al==0 and bl >= 2 :
            result += bBC[0][0] 
        elif bl == 0 and al == 1 :
            result += aBC[0][0]
        elif bl == 0 and al >= 2 :
            result += aBC[0][0] 
        
        elif al == 1 and bl == 1 :
            if aBC[0][1] != bBC[0][1] :
                result += aBC[0][0] + bBC[0][0]
            else :
                result += aBC[0][0]
        
        elif al == 1 and bl >= 2 :
            result += aBC[0][0]
            for b in bBC :
                if b[1] != aBC[0][1] :
                    result += b[0]
                    break
        elif bl == 1 and al >= 2 :
            result += bBC[0][0]
            for a in aBC :
                if a[1] != bBC[0][1] :
                    result += a[0]
                    break
        elif al >= 2 and bl >= 2 :
            if aBC[0][1] != bBC[0][1] :
                result += aBC[0][0] + bBC[0][0]
            else :
                result += (aBC[0][0] + max(aBC[1][0],bBC[1][0]))
        m += 1

    print('#{} {}'.format(test_case,result))



    