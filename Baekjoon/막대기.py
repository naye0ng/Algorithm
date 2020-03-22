"""
막대기
https://www.acmicpc.net/problem/1094
"""

N = sum(map(int, " ".join(format(int(input()), 'b')).split()))
print(N)

"""
23을 만든다.

64 
32
16 16
16 8
16 4 4
16 4 2 2
16 4 2 1 >> 23의 이진수 표현
"""