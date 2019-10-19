"""
수영장
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE
"""
def DFS(m, cost) :
    if m >= 12 :
        global low_cost
        low_cost = min(low_cost, cost)
    else :
        # 하루
        DFS(m+1, cost+cnt[m]*day)
        # 한달
        DFS(m+1, cost+month)
        # 세달치
        DFS(m+3, cost+month3)

T = int(input())
for test_case in range(1,1+T) :
    day, month, month3, low_cost = map(int, input().split())
    cnt = list(map(int, input().split()))
    DFS(0, 0) 
    print('#{} {}'.format(test_case, low_cost)) 
