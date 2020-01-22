"""
연산자끼워넣기
https://www.acmicpc.net/problem/14888
"""
maxAnswer, minAnswer = -1000000000, 1000000000
def makeOpers(N, n, answer) :
    if N == n :
        global maxAnswer, minAnswer 
        maxAnswer = max(maxAnswer, answer)
        minAnswer = min(minAnswer, answer)
    else :
        # 남아있는 연산자 중애서 하나씩 선탣
        for i in range(4) :
            if opers[i] > 0 :
                opers[i] -= 1
                if i == 0 :
                    makeOpers(N, n+1, answer + numbers[n])
                elif i == 1 :
                    makeOpers(N, n+1, answer - numbers[n])
                elif i == 2 :
                    makeOpers(N, n+1, answer * numbers[n])
                elif i == 3 :
                    if answer < 0 :
                        local = -1*answer
                        makeOpers(N, n+1, (local // numbers[n])*-1)
                    else :
                        makeOpers(N, n+1, answer // numbers[n])                   
                opers[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

makeOpers(N, 1, numbers[0])
print(maxAnswer)
print(minAnswer)
