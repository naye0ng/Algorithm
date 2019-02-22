"""
1966.숫자를 정렬하자
"""


T = int(input())
for test_case in range(1, T+1) :
    n = int(input())
    an = list(map(int, input().split()))

    # 퀵소트 구현해보자