"""
이진수2
"""
import sys
sys.stdin = open('input.txt','r')

def binary(t, result='') :
    if len(result) > 12 :
        return 'overflow'
    elif t == 0 :
        return result
    else :
        result += str(int(t*2//1))
        return binary((t*2)%1,result)


T = int(input())
for test_case in range(1,1+T) :
    N = float(input())
    print('#{} {}'.format(test_case, binary(N)))