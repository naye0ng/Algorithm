"""
4869.종이 붙이기
"""
def box(n) :
    if n == 10 :
        return 1
    if n == 20 :
        return 3
    return box(n-10)+box(n-20)*2

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {box(n)}')