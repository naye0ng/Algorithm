"""
1986.지그재그 숫자
"""
T = int(input())
for test_case in range(1,T+1) :
    result = 0
    for i in range(1, int(input())+1):
        if i%2 :
            result+=i
            continue
        result-=i
    
    print(f'#{test_case} {result}')