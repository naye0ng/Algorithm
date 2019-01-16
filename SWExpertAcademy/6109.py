"""
6109.추억의 2048게임
"""
T = int(input())

for test_case in range(1, T + 1):
    n, motion = input().split()
    n = int(n)

    an = [[i for i in map(int,input().split())] for j in range(n)]
    bn = [[0]*n for i in range(n)]

    if motion == 'up':
        bn[0] = an[0]
        for i in range(1,n):
            for j in range(n) :
                if an[i][j] == 0 :
                    continue
                for k in range(i-1,-1,-1) :
                    if bn[k][j] != 0 :
                        if bn[k][j] == an[i][j] :
                            bn[k][j] = str(an[i][j]*2)
                        else :
                            bn[k+1][j] = an[i][j]
                        break
                    elif k==0 :
                        bn[k][j] = an[i][j]
    elif motion == 'down' :
        bn[n-1] = an[n-1]
        for i in range(n-1,-1,-1):
            for j in range(n) :
                if an[i][j] == 0 :
                    continue
                for k in range(i+1,n) :
                    if bn[k][j] != 0 :
                        if bn[k][j] == an[i][j] :
                            bn[k][j] = str(an[i][j]*2)
                        else :
                            bn[k-1][j] = an[i][j]
                        break
                    elif k==(n-1) :
                        bn[k][j] = an[i][j]
    elif motion == 'left' :
        for i in range(n) :
            bn[i][0] = an[i][0]
            for j in range(1,n) :
                if an[i][j]==0:
                    continue
                for k in range(j-1,-1,-1):
                    if bn[i][k] != 0 :
                        if bn[i][k] == an[i][j] :
                            bn[i][k] = str(an[i][j]*2)
                        else :
                            bn[i][k+1] = an[i][j]
                        break
                    elif k==0 :
                        bn[i][k] = an[i][j]
    elif motion == 'right' :
        for i in range(n) :
            bn[i][n-1] = an[i][n-1]
            for j in range(n-2,-1,-1) :
                if an[i][j] == 0:
                    continue
                for k in range(j+1,n) :
                    if bn[i][k] != 0 :
                        if bn[i][k] == an[i][j] :
                            bn[i][k] = str(an[i][j]*2)
                        else :
                            bn[i][k-1] = an[i][j]
                        break
                    elif k == (n-1) :
                        bn[i][k] = an[i][j]



    print(f'#{test_case}')
    for i in range(n) :
        print(" ".join(map(str, bn[i])))
                

