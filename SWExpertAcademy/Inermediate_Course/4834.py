"""
4834.숫자 카드 
"""

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    an = list(map(int,input().replace(""," ").split()))
    
    count = 0
    max_num = 0
    for i in range(1,10) :
        if i in an :
            if an.count(i) >= count :
                count = an.count(i)
                max_num = i

    print(f'#{test_case} {max_num} {count}')

