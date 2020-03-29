"""
탑
https://www.acmicpc.net/problem/2493
"""
N = int(input())
height = list(map(int, input().split()))
recive = ['0' for _ in range(N)]

for h in range(N-1, -1, -1) :
    # 수신탑 찾기
    for k in range(h-1,-1,-1) :
        if height[k] >= height[h] :
            recive[h] = str(k+1)
            break
print(" ".join(recive))