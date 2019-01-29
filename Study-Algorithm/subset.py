"""
부분집합의 합
"""
arr = list(map(int,input().split()))

n = len(arr)

#n개의 부분집합 생성
# 공집합을 처리하는 경우 0부터, 아니라면 1부터 1<<n까지 수행
for i in range(1 << n) :
    ssum = 0
    sub = []
    for j in range(n) :
        #n개 자리수랑 shift및 &연산
        if i & (1<<j) :
            # 해당하는 수가 부분집합에 있다!
            ssum += arr[j]
            sub.append(arr[j])

    if ssum == 0 :
        print(sub)