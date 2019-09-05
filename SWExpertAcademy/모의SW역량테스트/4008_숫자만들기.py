"""
4008 - 숫자 만들기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE
"""

def operOrder(N,depth,value) :
    if N == depth :
        # 실제 연산 수행
        global maxV, minV 
        maxV = max(maxV,value)
        minV = min(minV,value)
    else :
        # 연산자는 4개 뿐이므로 연산자의 갯수만 체크해서 순열을 만들면 중복을 효율적으로 줄일 수 있다.
        for i in range(4) :
            if opers[i] > 0 :
                opers[i] -= 1
                if i == 0 :
                    operOrder(N,depth+1,value+numbers[depth+1])
                elif i == 1 :
                    operOrder(N,depth+1,value-numbers[depth+1])
                elif i == 2 :
                    operOrder(N,depth+1,value*numbers[depth+1])
                elif i == 3 :
                    # python에서의 음수를 나눌때 -2//-3은 -1이 아닌 -2가된다. 
                    # 이 문제에서 나눗셈 후, 나머지를 버린다고 했으므로 아래와 같은 방법이 올바르다.
                    operOrder(N,depth+1,int(value/numbers[depth+1]))
                opers[i] += 1

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())

    opers = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    maxV, minV = -100000000, 100000000
    operOrder(N-1,0,numbers[0])

    print('#{} {}'.format(test_case,maxV-minV))

"""
1
5
2 1 0 1
3 5 3 7 9
"""