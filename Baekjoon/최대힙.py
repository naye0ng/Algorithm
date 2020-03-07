"""
최대힙
https://www.acmicpc.net/problem/11279
"""

"""
[시간초과]
""" 
# import heapq

# N = int(input())
# h = []
# for _ in range(N) :
#     n = int(input())
#     if n == 0 :
#         if h :
#             print(-heapq.heappop(h))
#         else :
#             print(0)
#     else :
#         heapq.heappush(h, -n)


"""
input() vs sys.stdin.readlines()
- input()의 경우, 변수의 형태를 가공하기 위해 input()메소드 내에서 가공이 일어난다.
- [속도 빠르기 비교] sys.stdin.readline() > raw_input() > input()
- https://www.acmicpc.net/blog/view/56
"""
import sys
import heapq

N = int(input())
h = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 :
        if h :
            print(-heapq.heappop(h))
        else :
            print(0)
    else :
        heapq.heappush(h, -n)
