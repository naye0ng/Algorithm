"""
소수의 나열2
에라토스테네스의 체를 이용 

- 2부터 n까지의 배열을 생성한다.
- 소수의 판별 : 소수의 배수는 소수가 아니므로 0으로 마킹 >> 마지막엔 소수만 남는다.
- 최적화 : 이전에 마킹된 값은 처리하지 않음! >> 이거 안하면 최악의 경우가 생김
"""

def decimal(x) :
    decimals = [i for i in range(2,x+1)]

    for i in decimals :
        if i == 0 :
            continue

        # 0으로 배수 마킹 
        j = decimals.index(i)+i

        while j < len(decimals) :
            if decimals[j] == 0 :
                j += i
                continue
            if decimals[j]%i == 0 :
                decimals[j] = 0
            j += i
    
    return [i for i in decimals if i !=0]

print(decimal(10000))