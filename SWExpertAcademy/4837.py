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
                ansum+=an[j]
        #여기까지가 부분집합 1번
        if count == n and ansum == k :
            result+=1

    print(f'#{test_case} {result}')
