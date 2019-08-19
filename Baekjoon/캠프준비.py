"""
캠프준비
https://www.acmicpc.net/problem/16938
"""

count = 0
def getAlgorithm(N, L, R, X, n, depth, arr):
    #  count 계산
    if depth >= 2 and (arr[-1]-arr[0]) >= X :
        s = sum(arr)
        if s >= L and s <= R :
            global count 
            count += 1
    if depth <= N :
        for i in range(n, N) :
            if visited[i] == False :
                visited[i] = True
                getAlgorithm(N, L, R, X, i, depth+1, arr+[an[i]])
                visited[i] = False
 

N, L, R, X = map(int, input().split())
an = list(map(int, input().split()))
an.sort()
visited = [False]*N
getAlgorithm(N, L, R, X, 0, 0, [])
print(count)