"""
4865.글자수
"""
T = int(input())
for test_case in range(1, T + 1):
    p = input().replace(""," ").split()
    an = input().replace(""," ").split()

    # 패턴글자를 키값(중복제거)으로 딕셔너리 생성
    dict_an = {}
    for value in p :
        dict_an[value] = 0

    # 패턴 글자수 세기, 더불어 max_s도 찾기
    max_s = 0
    for i in an :
        if i in dict_an.keys() :
            dict_an[i] +=1
            if max_s < dict_an[i] :
                max_s = dict_an[i]

    print(f'#{test_case} {max_s}')
