from itertools import combinations

def solution(answer_sheet, sheets):
    answer = 0

    comb = combinations(sheets, 2)
    for p1, p2 in comb :
        total, connect, max_connect = 0, 0, 0

        for i in range(len(answer_sheet)) :
            # 같은 선택지를 골랐으나 오답인 경우
            if p1[i] == p2[i] and p1[i] != answer_sheet[i] :
                connect += 1
                total += 1
            else :
                connect = 0
            max_connect = max(max_connect, connect)
        answer = max(answer, total+(max_connect**2))
    
    return answer

print(solution("4132315142",["3241523133","4121314445","3243523133","4433325251","2412313253"]))