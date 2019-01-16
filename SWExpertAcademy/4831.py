"""
4831.전기버스
"""

T = int(input())

for test_case in range(1, T + 1):
    # 한번 충전으로 k개 이동
    k,n,m = map(int,input().split())
    #충전기가 설치된 정류장
    am = list(map(int, input().split()))

    count = 0
    i = 0
    while i < n-k :
        # n-k까지로 해야 점프 구간이 k개 이하일때 멈춤
        # i, i+k 사이에 am이 있어야함
        not_in = 0
        for j in range(i+k,i,-1):
            if j in am :
                # 사이값 중 가장 큰 것
                not_in = 1
                count+=1
                i = j
                break

        if not_in == 0 :
            # 사이에 아무것도 없음, while 종료
            count=0
            break
                
    print(f'#{test_case} {count}')