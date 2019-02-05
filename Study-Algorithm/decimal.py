""" 
소수의 나열

- 배열에 소수를 누적하여 저장한다.
- 소수판별 : 이전에 배열에 누적된 소수들로도 나눠지지 않아야 소수
- 최적화 : 2는 배열에 넣고 시작, 짝수는 소수가 아니므로 반복문을 2씩 증가
"""

# decimal(x) : 1~x까지의 소수 배열을 반환하는 함수
def decimal(x) :
    decimals = [2]

    i = 3 
    while i <= x :
        l = 0
        for j in range(len(decimals)) :
            if i%decimals[j] == 0 :
                break
            l+=1

        # for 루프 다 돌았는지 확인
        if l == len(decimals) :
            decimals.append(i)

        # 짝수 제외
        i+=2
    
    return decimals

print(decimal(10000))