"""
1216.회문3
"""

def pelin(s) :
    l = len(s)
    max = 1
    for i in range(l) :
        for j in range(l) :
            # max값보다 적게 남으면 for 루프 생략한다.
            if l-j <= max :
                break

            # s[i][j]를 시작으로 펠린드롭 비교 >> 인덱스가 뒤에서부터 준다. >> 끝점은 k
            for k in range(l-1,j,-1) :
                # 비교할 문자열의 갯수
                m = k-j+1
                # print(i, "행", j, "열")
                # 비교할 갯수가 max보다 작으면 스톱
                if m <= max :
                    break;
                #문자열 비교
                check = 0
                for p in range(m//2) :
                    # 팰린드롭 아니면 멈춤
                    if s[i][j+p] != s[i][k-p] :
                        break
                    # print(s[i][j+p], s[i][k-p])
                    check+=1
                # 팰린드롭이 맞다면 max값 증가 및 for루프 중단
                if check == m//2 :
                    if max < m :
                        # print(m)
                        max = m
    return max

def pelin2(s, max) :
    l = len(s)
    for i in range(l) :
        for j in range(l) :
            # max값보다 적게 남으면 for 루프 생략한다.
            if l-j <= max :
                break

            # s[i][j]를 시작으로 펠린드롭 비교 >> 인덱스가 뒤에서부터 준다. >> 끝점은 k
            for k in range(l-1,j,-1) :
                # 비교할 문자열의 갯수
                m = k-j+1
                # print(i, "행", j, "열")
                # 비교할 갯수가 max보다 작으면 스톱
                if m <= max :
                    break;
                #문자열 비교
                check = 0
                for p in range(m//2) :
                    # 팰린드롭 아니면 멈춤
                    if s[j+p][i] != s[k-p][i] :
                        break
                    check+=1
                # 팰린드롭이 맞다면 max값 증가 및 for루프 중단
                if check == m//2 :
                    if max < m :
                        # print(m)
                        max = m
    return max


for t in range(10):
    test_case = int(input())
    an = [input().replace("", " ").split() for i in range(100)]

    count_max = pelin(an)
    print(f'#{test_case } {pelin2(an,count_max)}')