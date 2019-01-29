"""
2007.패턴 마디의 길이
"""

T = int(input())
for test_case in range(1, T + 1):

    an = input().replace(""," ").split()

    # 패턴의 횟수를 센다면,
    # 패턴의 반복이므로 글자 수를 세자! 
    # 같은 숫자가 두 번 이상 들어가더라도 전체 글자 수의 최소값을 구하므로 상관 없다.
    dict_an = {}
    for value in an :
        dict_an[ord(value)] = dict_an.get(ord(value),0)+1
    values = dict_an.values()
    count = min(values)
    
    # 이 문제는 패턴의 횟수가 아니라 패턴의 길이를 구하는 문제(문제를 잘 읽읍시다!!!)
    # 패턴의 수(위에서 구한거)로 각 글자를 나눈 몫을 더한다 >> 그게 한 패턴에 그 문자가 들어가는 횟수이므로 다 더하면 패턴의 길이가 된다.
    length = sum([i//count for i in values])
    
    print(f'#{test_case} {length}')