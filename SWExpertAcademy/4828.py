"""
4828.min max
"""
# min, max함수 구현
def max(an) :
    max_n = an[0]
    for a in an :
        if max_n < a :
            max_n = a
    return max_n

def min(an) :
    min_n = an[0]
    for a in an :
        if min_n > a :
            min_n = a
    return min_n

# 아예 한번에 값을 리턴
def min_max(an) :
    max_n = an[0]
    min_n = an[0]
    for i in range(1,len(an)) :
        if max_n < an[i] :
            max_n = an[i]
        if min_n > an[i] :
            min_n = an[i]
    return max_n-min_n


t = int(input())

for i in range(1,t+1) :
    n = int(input())
    an = list(map(int, input().split()))
    
    print(f'#{i} {max(an)-min(an)}')
