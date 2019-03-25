"""
1240.단순 2진 암호코드
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,1+T) :
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    empty =str(0)*M

    # 암호문이 들어있는 행 찾기
    target = 0, []
    for n in range(N) :
        if arr[n] != empty :
            # 암호문 배열 반환 
            # 이 부분은 python의 mat함수
            for i in range(M-1,-1,-1) :
                if arr[n][i] == '1' :
                    target = [ arr[n][k-7:k] for k in range(i-48, i+6, 7)]
                    break
            break
    # replace말고 dictionary를 사용하는 것도 고려하자.
    for i in range(8) :
        target[i] = target[i].replace('0001101', '0')
        target[i] = target[i].replace('0011001', '1')
        target[i] = target[i].replace('0010011', '2')
        target[i] = target[i].replace('0111101', '3')
        target[i] = target[i].replace('0100011', '4')
        target[i] = target[i].replace('0110001', '5')
        target[i] = target[i].replace('0101111', '6')
        target[i] = target[i].replace('0111011', '7')
        target[i] = target[i].replace('0110111', '8')
        target[i] = target[i].replace('0001011', '9')

    if ((int(target[0])+int(target[2])+int(target[4])+int(target[6]))*3+int(target[1])+int(target[3])+int(target[5])+int(target[7]))%10 :
        result = 0
    else :
        result = sum(map(int, target))
    print('#{} {}'.format(test_case,result))
