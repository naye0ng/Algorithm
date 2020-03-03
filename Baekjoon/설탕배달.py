"""
설탕배달
https://www.acmicpc.net/problem/2839
""" 
N = int(input())

# 5의 배수가 나올때까지 3을 뻰다.
n3, n5 = 0, 0
while N >= 3 :
    if N%5 == 0 :
        n5 += N//5
        N = 0
    else :
        N -= 3
        n3 += 1

if N == 0 :
    print(n3+n5)
else :
    print(-1)
