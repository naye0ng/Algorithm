N = int(input())
arr = list(map(int, input().split()))

dist = 1000000
for x in range(N-1) :
    dist = min(dist, arr[x+1]-arr[x])
print(dist)

"""
5
1 9 29 59 60

답 : 1
"""