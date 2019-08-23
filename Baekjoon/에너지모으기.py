"""
에너지모으기
https://www.acmicpc.net/problem/16198
"""

E = 0
def getEnerge(N, e, wn) :
    if N == 2:
        global E
        E = max(E,e) 
    else :
        for x in range(1, N-1) :
            e += ( wn[x-1] * wn[x+1] )
            getEnerge(N-1,e,wn[:x]+wn[x+1:])
            e -= ( wn[x-1] * wn[x+1] )

N = int(input())
arr = list(map(int, input().split()))

getEnerge(N,0,arr)
print(E)