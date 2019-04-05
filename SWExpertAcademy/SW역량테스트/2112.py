"""
2112.보호 필름
"""
import sys
sys.stdin = open('input.txt','r')
# def test(n, arr) :
#     if isPass(arr) :
#         global result
#         if result > n :
#             result = n
#     if n < result :
#         for x in range(D) :
#             if not visited[x] and n+1 < result:
#                 temp = arr[:]
#                 visited[x] = 1
#                 # A, B 한번씩 변환
#                 temp[x] = [0]*W
#                 test(n+1,temp)
#                 temp[x] = [1]*W
#                 test(n+1,temp)
#                 visited[x] = 0
def isPass(arr) :
    # 세로줄 검사
    n = 0
    for y in range(W) :
        A, B = 0, 0
        for x in range(D) :
            if arr[x][y]:
                B += 1
                A = 0
            else :
                A+=1
                B = 0
            if A >= K or B >= K :
                n+=1
                break
        #만약 K개의 연속된 값이 없다면 정지
        if A < K and B < K :
            return False
    return True

# 부분집합으로 계산하기
def powerset(arr) :
    global result
    for i in range(1 << D) :
        n, breakPT = 0, False
        arrA = arr[:]
        arrB = arr[:]
        for j in range(D) :
            if i & (1 << j ) :
                n+=1
                if n >= result :
                    breakPT = True
                    break
                arrA[j] = [0]*W
                arrB[j] = [1]*W
        if not breakPT :
            if isPass(arrA) or isPass(arrB):
                if result > n:
                    result = n

T = int(input())
for test_case in range(1,1+T) :
    D, W, K = map(int, input().split())
    F = [list(map(int, input().split())) for _ in range(D)]
    visited = [0]*D
    result = D
    powerset(F)

    print('#{} {}'.format(test_case,result))