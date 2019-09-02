"""
무선충전
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE
"""

# 겹치는 것 검색
def getBC(N,x,y) :
    can_use = []
    for i in range(N) :
        bcX, bcY, c, p = battery_charger[i]
        if  abs(bcX-x)+abs(bcY-y) <= c :
            can_use.append([p,i])
    return sorted(can_use)

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

        A = getBC(N,ax,ay)
        B = getBC(N,bx,by)
        
        la = len(A)
        lb = len(B) 

        if la + lb = 1 and la > lb :
            pass
        elif la + lb = 1 and la < lb :
            pass
        elif la == 1 and lb == 1 :
            pass
        elif la == 1 and lb == 2 :
            pass

        # 한쪽이 0이라면?
        # if la == 0 or lb == 0 :
        #     result += sum(A[:1][:1]+B[:1][:1])
        # else :
        #     i = 0 
        #     if A[0][1] != B[0][1] :
        #         result += A[0][0] + B[0][0]
        #     else :
        #         # 같다면 처음꺼 저장
        #         result += A[0][0]
        #         # 두번째 준에 큰 값 저장



    print('#{} {}'.format(test_case,result))