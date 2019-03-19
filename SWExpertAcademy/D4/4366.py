"""
4366.정식이의 은행업무

-  2진수와 3진수의 값은 무조건 1자리씩 틀리다. 한자리씩 변환하여 같은 수를 반환해라
"""

import sys
sys.stdin = open('input.txt','r')

T= int(input())
for test_case in range(1, 1+T):
    n2 = input()
    n3 = input()
    l2, l3 = len(n2), len(n3)

    # 2진수 후보 찾아서 10진수로 저장하기
    arr2 = [0]*l2
    for i in range(l2) :
        if n2[i] == '1' :
            arr2[i] = int(n2[:i]+str(0)+n2[i+1:],2)
        else :
            arr2[i] = int(n2[:i] + str(1) + n2[i + 1:],2)

    # 3진수 후보 찾아서 검사
    result = 0
    for j in range(l3) :
        if n3[j] != '0' :
            n = int(n3[:j] + str(0) + n3[j + 1:], 3)
            if n in arr2 :
                result = n
                break
        if n3[j] != '1' :
            n = int(n3[:j] + str(1) + n3[j + 1:], 3)
            if n in arr2 :
                result = n
                break
        if n3[j] != '2' :
            n = int(n3[:j] + str(2) + n3[j + 1:], 3)
            if n in arr2 :
                result = n
                break

    print('#{} {}'.format(test_case, result))