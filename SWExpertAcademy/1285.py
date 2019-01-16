"""
1285. 아름이의 돌 던지기

N명의 사람들이 던진 돌이 떨어진 위치를 측정한 자료가 주어질 때, 
가장 0에 가깝게 돌이 떨어진 위치와 0 사이의 거리 차이와 
몇 명이 그렇게 돌을 던졌는지를 구하는 프로그램을 작성하라.

input)
2
2
-100 100
3
-5 -1 3

output)
#1 100 2
#2 1 1
"""

t= int(input())
for i in range(t) :
    #사실 n은 필요가 없음
    n = input()
    
    # 절대값으로 바꿔서 정렬
    k = list(map(abs,map(int,input().split())))
    k.sort()
    
    print(k.count(k[0]))

    print(f'#{i+1} {k[0]} {k.count(k[0])}')