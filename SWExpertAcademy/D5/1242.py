"""
1242.암호코드 스캔
"""
import sys
sys.stdin = open('input.txt','r')

match = [[3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],[1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]]

T= int(input())
for test_case in range(1, 1+T):
    N, M = map(int, input().split())

    # 중복되는 암호문 입력 안받음
    empty = str(0)*M
    arr = [0]*N
    n = -1
    for _ in range(N) :
        local = input()
        if local != empty :
            if n== -1 or arr[n] != local :
                n+=1
                arr[n] = local
    n +=1
    arr = arr[:n]

    # 이진수 변환
    for x in range(n) :
        arr[x] = arr[x].replace('0', '0000')
        arr[x] = arr[x].replace('1', '0001')
        arr[x] = arr[x].replace('2', '0010')
        arr[x] = arr[x].replace('3', '0011')
        arr[x] = arr[x].replace('4', '0100')
        arr[x] = arr[x].replace('5', '0101')
        arr[x] = arr[x].replace('6', '0110')
        arr[x] = arr[x].replace('7', '0111')
        arr[x] = arr[x].replace('8', '1000')
        arr[x] = arr[x].replace('9', '1001')
        arr[x] = arr[x].replace('A', '1010')
        arr[x] = arr[x].replace('B', '1011')
        arr[x] = arr[x].replace('C', '1100')
        arr[x] = arr[x].replace('D', '1101')
        arr[x] = arr[x].replace('E', '1110')
        arr[x] = arr[x].replace('F', '1111')

    patt = []
    maxPattern = 0
    #암호문 찾기
    for x in range(n) :
        end, start = 0, 0
        for y in range(len(arr[x])-1,-1,-1) :
            if end == 0 and arr[x][y] == '1':
                end = y+1
            elif start == 0 and end != 0 and arr[x][y] == '0' :
                start = y+1
                # 0이 나오더라도 길이가 부족하면 앞쪽 다시 탐색
                if (end - start)%56 :
                    start = 0
                else :
                    lengthP = (end - start)//56
                    an = arr[x][start:end]
                    # 패턴의 유효성 검사, 마지막 글자는 항상 1
                    # 패턴 유효성 검사, 맨 앞의 '0'은 최대 lengthP만큼
                    is_pattern = True
                    for i in range(0,len(an),7*lengthP) :
                        if '1' in an[i :i+lengthP] or an[i+lengthP*7-1] !='1' :
                            is_pattern = False
                            break

                    if is_pattern :
                        if maxPattern < lengthP :
                            maxPattern = lengthP
                        patt.append([lengthP, an])
                        end  = 0
                        start = 0
                    # 계속 앞으로 전진!
                    else :
                        start = 0

    # maxPattern만큼 패턴 딕셔너리 생성
    dictmatch = {}
    for i in range(1,maxPattern+1) :
        for j in range(10) :
            dictmatch[str(0)*match[j][0]*i+str(1)*match[j][1]*i+str(0)*match[j][2]*i+str(1)*match[j][3]*i] = str(j)

    # 중복제거한 패턴 리스트
    Pattern = []
    for p in patt :
        pn = ''
        for k in range(0,p[0]*56-1,7*p[0]) :
            pn += dictmatch[p[1][k:k+7*p[0]]]
        if pn not in Pattern :
            Pattern.append(pn)

    # 올바른 패턴인지 검사
    result = 0
    for i in range(len(Pattern)) :
        pn = list(map(int,Pattern[i].replace('', ' ').split()))
        if ((pn[0]+pn[2]+pn[4]+pn[6])*3+(pn[1]+pn[3]+pn[5])+pn[7])%10 == 0:
            result += sum(pn)

    print('#{} {}'.format(test_case, result))

