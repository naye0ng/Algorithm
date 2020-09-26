'''
지능형기차2
https://www.acmicpc.net/problem/2460
'''

train, max_passenger = 0, 0
for _ in range(10) :
    down, up = map(int, input().split())
    train -= down
    train += up
    max_passenger = max(max_passenger, train)

print(max_passenger)