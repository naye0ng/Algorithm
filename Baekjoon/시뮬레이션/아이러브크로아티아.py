'''
아이러브크로아티아
https://www.acmicpc.net/problem/9517
'''
K = int(input())-1
N = int(input())
Q = [input().split() for _ in range(N)]

time = 0
while time < 210 :
    sec, answer = Q.pop(0)
    time += int(sec)

    if answer == 'T' :
        if time >= 210 : break
        K = (K+1)%8

print(K+1)