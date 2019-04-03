"""
4008.숫자 만들기
"""
import sys
sys.stdin = open('input.txt','r')

OP = ['+', '-','*','/']

def getMinMax(n, t1) :
    if n == N-1 :
        global minV, maxV
        if minV > t1 :
            minV = t1
        if maxV < t1 :
            maxV = t1
    else :
        for i in range(4) :
            t2 = number[n+1]
            if arr[i] == 0 :
                continue
            if OP[i] == '+' :
                t = t1+t2
                arr[i] -= 1
                getMinMax(n+1,t)
                arr[i] += 1
            elif OP[i] == '-' :
                t = t1 - t2
                arr[i] -= 1
                getMinMax(n + 1, t)
                arr[i] += 1
            elif OP[i] == '*' :
                t = t1*t2
                arr[i] -= 1
                getMinMax(n + 1, t)
                arr[i] += 1
            elif OP[i] == '/' :
                if t1 < 0 :
                    t = abs(t1)//t2*(-1)
                else :
                    t = t1//t2
                arr[i] -= 1
                getMinMax(n + 1, t)
                arr[i] += 1

T = int(input())
for test_case in range(1,1+T) :
    N = int(input())
    arr = list(map(int, input().split()))
    number = list(map(int, input().split()))
    minV, maxV = 1000000000, -1000000000
    getMinMax(0, number[0])
    print('#{} {}'.format(test_case,maxV-minV))