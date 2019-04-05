"""
1952.수영장
"""
import sys
sys.stdin = open('input.txt','r')

def getPrice(l,r) :
    if r-l == 3 :
        return min(M3,sum(M1[l:r]))
    if r-l < 2 :
        # 맨끝 11, 12 월 일때 3개월 쿠폰 추가
        if l >= 11 :
            return min(M3,sum(M1[l:r]))
        return sum(M1[l:r])
    price = 36001
    for i in range(r-1, l,-1) :
        left = getPrice(l,i)
        right = getPrice(i,r)
        temp = left+right
        if price > temp :
            price = temp
    return price

T = int(input())
for test_case in range(1,1+T) :
    D, M, M3, Y =  map(int, input().split())
    arr = list(map(int, input().split()))
    M1 = [ D*d if D*d < M else M for d in arr ]

    result = min(sum(M1),Y, getPrice(0,len(arr)))
    print('#{} {}'.format(test_case, result))