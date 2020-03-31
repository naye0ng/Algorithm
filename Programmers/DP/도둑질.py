def solution(money):
    N = len(money)
    dp = [0]*(N-1)
    dp2 = [0]*N
    dp[0] = money[0]
    # 처음을 포함 >> 인접한 두번째 값은 첫번째 값
    dp[1] = money[0]
    
    # 첫번째 값 미포함!
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2,N-1) :
        dp[i] = max(dp[i-2]+money[i],dp[i-1])
    for i in range(2, N) :
        dp2[i] = max(dp2[i-2]+money[i],dp2[i-1])
    
    return max(dp[-1], dp2[-1])