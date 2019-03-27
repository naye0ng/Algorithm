"""
5203.베이비진 게임
"""
import sys
sys.stdin = open('input.txt','r')

def winner(cl, cd, t) :
    cd[t] += 1
    # triplet
    if cd[t] >= 3 :
        return True
    # 동일한 숫자는 수행 안함
    elif cd[t] == 1 :
        i = 0
        while i < len(cl) :
            if t <= cl[i] :
                break
            i+=1
        cl.insert(i,t)
        # run찾기
        if i-1 >= 0 and t-cl[i-1] == 1 :
            if i-2 >= 0 and cl[i-1]-cl[i-2] == 1 :
                return True
            if i+1 < len(cl) and cl[i+1]-t == 1 :
                return True
        if i + 1 < len(cl) and cl[i + 1] - t == 1:
            if i+2 < len(cl) and cl[i+2]-cl[i+1] == 1 :
                return True
    return False

T = int(input())
for test_case in range(1,1+T) :
    cards = list(map(int, input().split()))

    result = 0
    num1, num2 = {i:0 for i in range(10)}, {i:0 for i in range(10)}
    card1, card2 = [], []
    for i in range(12) :
        if (i+1)%2 :
            if winner(card1,num1,cards[i]) :
                result= 1
                break
        else :
            if winner(card2,num2,cards[i]) :
                result = 2
                break

    print('#{} {}'.format(test_case, result))