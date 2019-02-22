"""
1284. 수도요금 경쟁

a: 리터당 p
b: 기본사용료 q, 월간이용료 r리터 이하인 경우 기본사용료만, 초과량 1리터당 s원

W: 사용자의 사용량
입력 순서:  P, Q, R, S, W
"""

t= int(input())

for i in range(t) :
    p,q,r,s,w = map(int, input().split())
    
    a = w*p
    b = q if w <= r else q+(w-r)*s
    
    print('#'+str(i+1),min(a,b))
