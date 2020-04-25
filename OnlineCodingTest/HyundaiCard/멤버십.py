end_date = [0,31,59,90,120,131,181,212,243,273,304,334,365]
def solution(purchase):
    membership = [0]*365
    for p in purchase :
        date, price = p.split()
        price = int(price)
        y, m, d = map(int, date.split("/"))
        # max는 365
        for i in range(end_date[m-1]+(d-1),min(365,end_date[m-1]+(d-1)+30)) :
            membership[i] += price

    answer = [0,0,0,0,0]
    for m in membership :
        if m < 10000 :
            answer[0] += 1
        elif m < 20000 :
            answer[1] += 1
        elif m < 50000 :
            answer[2] += 1
        elif m < 100000 :
            answer[3] += 1
        else :
            answer[4] += 1

    return answer

print(solution(	["2019/01/01 5000", "2019/02/01 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/07 100000"]))