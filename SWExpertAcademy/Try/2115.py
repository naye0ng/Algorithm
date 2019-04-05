"""
2115.벌꿀채취
"""
import sys
sys.stdin = open('input.txt','r')

def comb(n, m, c, a) :
    maxP = 0
    for i in range(n-m+1) :
        if m == 1 :
            if a[i] <= c :
                p = a[i] * a[i]
                if p > maxP:
                    maxP = p
        else :
            for j in range(i+1, n-(m-1)+1) :
                if m == 2 :
                    if a[i]+a[j] <= c :
                        p = a[i]*a[i]+a[j]*a[j]
                        if p > maxP:
                            maxP = p
                else :
                    for k in range(j+1, n-(m-2)+1) :
                        if m == 3 :
                            if a[i]+a[j]+a[k] <= c :
                                p = a[i]*a[i]+a[j]*a[j]+a[k]*a[k]
                                if p > maxP:
                                    maxP = p
                        else :
                            for p in range(k+1, n-(m-3)+1) :
                                if m == 4 :
                                    if a[i]+a[j]+a[k]+a[p] <= c :
                                        p = a[i]*a[i]+a[j]*a[j]+a[k]*a[k]+a[p]*a[p]
                                        if p > maxP:
                                            maxP = p
                                else :
                                    for q in range(p+1, n-(m-4)+1) :
                                        if a[i]+a[j]+a[k]+a[p]+a[q] <= c :
                                            p = a[i]*a[i]+a[j]*a[j]+a[k]*a[k]+a[p]*a[p]+a[q]*a[q]
                                            if p > maxP :
                                                maxP = p
    return maxP

T = int(input())
for test_case in range(1,1+T) :
    N, M, C = map(int, input().split())
    honey = [ list(map(int, input().split())) for _ in range(N) ]
    arr = []

    for x in range(N) :
        for y in range(N-M+1) :
            point = 0
            visited = []
            for i in range(1,M+1) :
                p = comb(M,i,C,honey[x][y:y+M])
                if p > point :
                    point = p
            arr.append([point,x,y])
    arr.sort(reverse=True)
    count,result,i  = 1,arr[0][0],1
    print(arr)
    while count :
        if arr[i][1] == arr[0][1] and abs(arr[i][2]- arr[0][2]) == M-1 :
            i+=1
            continue
        result+=arr[i][0]
        count-=1
    print('#{} {}'.format(test_case,result))
