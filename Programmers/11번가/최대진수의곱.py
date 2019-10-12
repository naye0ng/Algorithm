# k진수 변환
def convert(k, number) :
    convert_num = ''
    result = 1
    while number//k >= 1:
        next_number = number%k
        number = number//k
        convert_num = str(next_number) + convert_num

        if next_number != 0 :
            result *= next_number

        if number < k :
            convert_num = str(number) + convert_num
            if number != 0 :
                result *= number
    return result

def solution(N):
    maxK, maxN = 0, 0
    for k in range(9,1,-1) :
        subN = convert(k, N)
        if maxN < subN :
            maxK, maxN = k, subN

    return [maxK, maxN]