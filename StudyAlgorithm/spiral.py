"""
Spiral Algorithm
(나선형, 달팽이 알고리즘)

1. 등차수열 이용
"""
an = [[0]*6 for i in range(6)]
n = len(an)

sw = 1
i = 1
x = y = k = 0
while i <= n*n:
    if sw : 
        # y변화
        for j in range(y,n-k) :
            an[x][j] = i
            y =j
            i +=1
        # x변화
        x+=1
        for j in range(x,n-k) :
            an[j][y] = i
            x =j
            i+=1
        y-=1
        sw = 0

    else :
        # y변화 
        for j in range(y,0+k-1,-1) :
            an[x][j] = i
            y = j
            i+=1
        k+=1
        x-=1
        for j in range(x,0+k-1,-1) :
            an[j][y] = i
            x = j
            i+=1
        y+= 1
        sw = 1 

for e in range(n) :
    print(an[e])


