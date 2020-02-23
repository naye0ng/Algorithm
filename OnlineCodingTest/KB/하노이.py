# 기둥 : 시작 1, 임시는 2, 목표는 3
def hanoi(n, start, other, end) :
    if n == 1 :
        # 블록 이동
        return 1
    return sum([hanoi(n-1, start, end, other), hanoi(1, start, other, end),hanoi(n-1, other, start, end)])

N = int(input())
print(hanoi(N, 1, 2, 3))