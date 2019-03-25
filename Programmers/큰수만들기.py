"""
큰 수 만들기
"""
maxNum = ""

# 자리수가 정해져 있음, 중복 안됨 >> 조합으로 푼다.
def comb(number, temp, n, r, k, s) :
    if k == r :
        local = "".join(temp)
        global maxNum
        if maxNum < local :
            maxNum = local
        print(temp, maxNum)
    else :
        for i in range(s,n-r+k+1) :
            print(maxNum[k], number[i])
            temp[k] = number[i]
            comb(number,temp,n,r,k+1,i+1)

def solution(number, k):
    number = number.replace('',' ').split()
    n = len(number)
    r = len(number)-k
    temp = ["0"]*r

    global maxNum
    maxNum = "0" * r

    comb(number, temp, n, r, 0, 0)

    return maxNum

print(solution("1924", 2))