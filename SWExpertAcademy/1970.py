"""
1970.쉬운 거스름돈
"""
T = int(input())
for test_case in range(1,T+1) :
    price = int(input())

    
    man = price//10000
    price -= man*10000

    chun = price//1000
    price -= chun*1000

    back = price//100
    price -= back*100

    ssip = price//10

    print(f'#{test_case}')
    print(man//5,man-(man//5)*5, end=' ')
    print(chun//5,chun-(chun//5)*5, end=' ')
    print(back//5,back-(back//5)*5, end=' ')
    print(ssip//5,ssip-(ssip//5)*5)


    


