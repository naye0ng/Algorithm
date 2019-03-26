"""
큰 수 만들기
"""
def getNext(p,result) :
    for i in range(p,len(result)-1) :
        if result[i] < result[i+1] :
            return i
    return len(result)-1

def solution(number, k):
    number = list(map(int, number.replace('',' ').split()))
    n = len(number)
    r = n-k
    result = number[-r:]
    p = getNext(0,result)

    for i in range(n-r-1,-1,-1) :
        if number[i] >= result[0] :
            result.pop(p)
            result.insert(0,number[i])
            # result = [number[i]]+result[0:p]+result[p+1:]
            if p != r-1 :
                p = getNext(p, result)

    return "".join(map(str,result))

print(solution("1924", 2))
print(solution("4177252841", 4))