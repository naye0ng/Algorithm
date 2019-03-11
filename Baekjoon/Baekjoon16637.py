"""
16637.괄호 추가하기
(삼성검정입사시험)

https://www.acmicpc.net/problem/16637
"""
maxValue = -(2**31)

def goEnd(tn) :
    # 피연산자부터 들어온다고 가정
    p = tn[0]
    for i in range(1,len(tn),2) :
        if tn[i] == '+' :
            p += tn[i+1]
        elif tn[i] == '-' :
            p -= tn[i+1]
        else :
            p *= tn[i+1]
    return p

def getMax(pre,tn,k) :
    #tn은 연산자부터 나옴
    global maxValue
    end = goEnd([pre]+tn)
    if end > maxValue :
        maxValue = end
    # k이후부터 피연산자를 뽑음
    for i in range(k+1,len(tn)-1,2) :
        if tn[i+1] == '+' :
            local = tn[i]+tn[i+2]
        elif tn[i+1] == '-' :
            local = tn[i]-tn[i+2]
        else :
            local = tn[i] * tn[i+2]
        getMax(pre,tn[:i]+[local]+tn[i+3:],i+1)


N = int(input())
an = input().replace(""," ").split()
for i in range(0,N,2) :
    an[i] = int(an[i])

getMax(0,['+']+an,0)
print(maxValue)