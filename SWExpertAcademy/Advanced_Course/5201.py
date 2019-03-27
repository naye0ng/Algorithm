"""
5201.컨테이너 운반
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int, input().split())
    con = list(map(int, input().split()))
    trk = list(map(int, input().split()))

    con.sort(reverse=True)
    trk.sort(reverse=True)
    c, t, result  = 0, 0, 0
    while c < N and t < M :
        if trk[t] >= con[c] :
            result+= con[c]
            t+=1
        c+=1

    print('#{} {}'.format(test_case, result))