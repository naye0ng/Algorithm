"""
4837.부분집합의 합
"""
T = int(input())

for test_case in range(1, T + 1):
    an = [i for i in range(1,13)]

    n, k = map(int,input().split())

    result = 0
    #shift를 이용한 부분집합 구하기
    for i in range(1 << 12) :
        count, ansum = 0, 0
        for j in range(12) :
            if i & (1 << j) :
                # an[i]가 부분집합에 들어 있다면
                count+=1
                # 이부분은 an[j]가 j+1(an의 j번째값은 j+1)가 된다. >> 이부분에 들어왔다는 것은 j가 부분집합에 선택되었다는 말임
                # 즉, ansum+=an[j]가 아니라 ansum+=(j+1) : 
                ansum+=(j+1)
        #여기까지가 부분집합 1번
        if count == n and ansum == k :
            result+=1

    print(f'#{test_case} {result}')
