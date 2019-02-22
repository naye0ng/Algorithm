t = int(input())

for test_case in range(1,1+t) :
    k = int(input())
    price = list(map(int, input().split()))

    total = 0

    # for i in range(k-1) :
    #     pc = price[i]
    #     max_sell = 0
    #     for j in range(i+1,k) :
    #         if price[j]-pc > max_sell :
    #             max_sell = price[j]-pc
    #     total += max_sell
    # for i in range(k-1) :
    #     pc = max(price[i+1:])-price[i]
    #     if pc > 0 :
    #         total+=pc
    
    for i in range(k-1) :
        pc = sorted(price[i+1:])[-1:][0] - price[i]  
        if pc > 0 :
            total+=pc

    print(f'#{test_case} {total}')