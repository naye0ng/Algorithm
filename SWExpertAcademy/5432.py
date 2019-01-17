"""
5432.쇠막대기 자르기
"""
T = int(input())

for test_case in range(1, T + 1):
    # 레이저 분리 > a
    an = list(input().replace("()","a").replace(""," ").split())

    n = len(an)

    count = [0 for i in range(n)]
    pt=0
    result = 0
    # an을 순회하는 for문
    for i in range(n) :
        if an[i] == '(' :
            pt+=1
        elif an[i] == 'a' and pt!=0 :
            count[pt] +=1
        elif an[i] == ')' :
            tmp = count[pt]
            count[pt] = 0
            result += (tmp+1)
            pt -=1
            count[pt]+=tmp


    print(f'#{test_case} {result}')



    # result = 0

    # # while 1 :
    # #     if ')' not in an or '(' not in an :
    # #         break

    # for j in range(an.count(')')) :
    #     q= an.index(')')
    #     for i in range(q-1,-1,-1):
    #         if an[i] == '(' :
    #             p = i
    #             # 원래는 q-(p+1)+1 이므로 q-p로 씀
    #             result += q-p

    #             # 여기서 주의할 점: q가 p보다 인덱스가 크므로 먼저 삭제
    #             del an[q]
    #             del an[p]
    #             break


    # print(f'#{test_case} {result}')