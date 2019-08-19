"""
야구
https://www.acmicpc.net/submit/17281
"""
from itertools import permutations

maxScore = -1
def makeScore(N, players) :
    score = n = i = 0 
    for n in range(N):
        out = 0
        f1, f2, f3 = False, False, False
        while out < 3 :
            p = players[i]
            if roundN[n][p] == 1 :
                score += f3
                f1, f2, f3 = True, f1, f2
            elif roundN[n][p] == 2 :
                score += f2 + f3
                f1, f2, f3 = False ,True, f1
            elif roundN[n][p] == 3 :
                score += f1 + f2 + f3
                f1, f2, f3 = False, False ,True
            elif roundN[n][p] == 4 :
                score += f1 + f2 + f3 + 1
                f1, f2, f3 = False, False, False
            elif roundN[n][p] == 0 :
                out += 1
            i = (i+1)% 9
    global maxScore
    if maxScore < score :
        maxScore = score                           

N = int(input())
roundN = [ list(map(int, input().split())) for _ in range(N)]
arr = [ i for i in range(9)]
for P in permutations(arr[1:]):
    makeScore(N, P[:3]+(arr[0],)+P[3:])
print(maxScore)



