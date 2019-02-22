"""
1208.Flatten
"""

for test_case in range(1, 11):
    #덤프 횟수
    count = int(input())
    an = list(map(int, input().split()))

    for dump in range(count) :
        #dump 한번당 자리 바꾸기 실행
        an[an.index(max(an))]-=1
        an[an.index(min(an))]+=1
    print(an)
    print(f'#{test_case} {max(an)-min(an)}')

