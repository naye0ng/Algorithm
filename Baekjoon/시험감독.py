"""
시험감독
https://www.acmicpc.net/problem/13458
"""

N = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())

total, i = 0, 0
while i < N :
    target = student[i]-B
    # 총감독관 한명으로 충분
    if target <= 0 :
        total += 1
    else :
        total += 1 + target//C
        if target % C :
            total +=1
    i += 1
print(total)