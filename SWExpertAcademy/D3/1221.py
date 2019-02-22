"""
1221.GNS
"""
t= int(input())
for test_case in range(1,t+1):
    n = input()
    str_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    number = [0]*10
    an = list(input().split())

    for i in range(len(an)):
        # 인덱스 찾기
        for j in range(10) :
            if an[i] == str_num[j] :
                number[j]+=1
                break
                
    print(f'#{test_case}')
    for i in range(10):
        print((str_num[i]+" ")*number[i],end='')



